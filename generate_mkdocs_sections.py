import ast
import os
import re
from collections import OrderedDict

# Paths
ROOTFS = "C:/Users/Sira/Documents/GitHub/exitOS/exitos/rootfs"
DOCS_DIR = "c:/Users/Sira/Desktop/exitOS_Documentation/exitOs/docs"

GROUPS = {
    "Server": [os.path.join(ROOTFS, "server.py")],
    "SqlDB": [os.path.join(ROOTFS, "sqlDB.py")],
    "Forecaster": [os.path.join(ROOTFS, "forecast/ForecasterManager.py"), os.path.join(ROOTFS, "forecast/Forecaster.py"), os.path.join(ROOTFS, "forecast/ForecastMetrics.py")],
    "Optimizer": [os.path.join(ROOTFS, "optimization/OptimalScheduler.py"), os.path.join(ROOTFS, "optimization/FlexibilityManager.py")],
    "Assets": [os.path.join(ROOTFS, "abstraction/assets/EVCharger.py"), 
               os.path.join(ROOTFS, "abstraction/assets/ShellyPlus1pm.py"), 
               os.path.join(ROOTFS, "abstraction/assets/SonnenBattery.py")]
}

# Global Registry: name -> {group, module, region, filename}
GLOBAL_REGISTRY = {}

def parse_doc(docstring):
    if not docstring:
        return {"desc": "Sense descripció.", "params": {}, "return": None}
    
    lines = docstring.strip().split("\n")
    desc_lines = []
    params = {}
    return_val = None
    
    current_param = None
    
    for line in lines:
        line_clean = line.strip()
        if line_clean.startswith(":param"):
            match = re.match(r":param\s+(\w+):\s*(.*)", line_clean)
            if match:
                current_param = match.group(1)
                params[current_param] = match.group(2)
            else:
                current_param = None
        elif line_clean.startswith(":return:"):
            return_val = line_clean.replace(":return:", "").strip()
            current_param = None
        elif line_clean.startswith(":"):
            current_param = None
        else:
            if current_param:
                params[current_param] += "\n" + line_clean
            elif return_val is not None:
                return_val += "\n" + line_clean
            else:
                desc_lines.append(line)
        
    # Final cleanup to support lists and manual breaks
    for p in params:
        params[p] = params[p].strip().replace("\\n", "\n")
    if return_val:
        return_val = return_val.strip().replace("\\n", "\n")
                
    return {
        "desc": "\n".join(desc_lines).strip(),
        "params": params,
        "return": return_val
    }

def get_params_list(node):
    if not hasattr(node, 'args'): return []
    args = []
    for arg in node.args.args:
        if arg.arg != 'self':
            args.append(arg.arg)
    return args

def extract_route(node):
    if not hasattr(node, "decorator_list"):
        return None
    for dec in node.decorator_list:
        if isinstance(dec, ast.Call):
            func = dec.func
            if isinstance(func, ast.Attribute) and func.attr in ["get", "post", "route"]:
                if dec.args and isinstance(dec.args[0], ast.Constant):
                    return dec.args[0].value
    return None

def get_method_labels(node):
    labels = []
    route = extract_route(node)
    if route:
        labels.append(f"Route: {route}")
    
    if hasattr(node, "decorator_list"):
        for dec in node.decorator_list:
            if isinstance(dec, ast.Name):
                if dec.id == "staticmethod":
                    labels.append("Mètode Estàtic")
                elif dec.id == "classmethod":
                    labels.append("Mètode de Classe")
    return labels

def has_return_stmt(node):
    if isinstance(node, ast.ClassDef):
        return True 
    for subnode in ast.walk(node):
        if isinstance(subnode, ast.Return):
            if subnode.value is not None:
                if isinstance(subnode.value, ast.Constant) and subnode.value.value is None:
                    continue
                return True
    return False

def generate_example_call(name, params, is_class=False, has_return=True):
    is_init = name.endswith(".__init__") or name == "__init__"
    
    if len(params) > 3:
        param_str = ",\n    ".join([f"{p}=..." for p in params])
        call_str = f"{name}(\n    {param_str}\n)"
    else:
        param_str = ", ".join([f"{p}=..." for p in params])
        call_str = f"{name}({param_str})"
    
    if is_class:
        return f"```python\nobj = {call_str}\n```"
    elif is_init:
        return f"```python\n{call_str}\n```"
    elif has_return:
        return f"```python\nresultat = {call_str}\n```"
    else:
        return f"```python\n{call_str}\n```"

def pretty_print_code(code_str):
    import json, ast
    # Try json
    try:
        obj = json.loads(code_str)
        return json.dumps(obj, indent=4)
    except:
        pass
    # Try ast
    try:
        obj = ast.literal_eval(code_str)
        if isinstance(obj, (dict, list, tuple)):
            import pprint
            return pprint.pformat(obj, indent=4, sort_dicts=False, width=80)
    except:
        pass
        
    # Fallback to naive formatter for pseudocode like [[ID, FriendlyName], ...]
    # If it's short, keep it on one line
    if len(code_str) < 80:
        return re.sub(r'\s+', ' ', code_str).strip()

    # Pre-clean the code string to remove existing inconsistent formatting and newlines
    code_str = re.sub(r'\s+', ' ', code_str).strip()

    formatted = ""
    indent = 0
    stack = []
    in_string = False
    string_char = None
    
    i = 0
    while i < len(code_str):
        char = code_str[i]
        if char in ('"', "'") and (i == 0 or code_str[i-1] != '\\'):
            if not in_string:
                in_string = True
                string_char = char
            elif string_char == char:
                in_string = False
            formatted += char
        elif not in_string:
            if char in ('{', '[', '('):
                stack.append(char)
                indent += 4
                if char == '{':
                    formatted += char + '\n' + (' ' * indent)
                else:
                    formatted += char
            elif char in ('}', ']', ')'):
                if stack: stack.pop()
                indent -= 4
                if char == '}':
                    formatted += '\n' + (' ' * indent) + char
                else:
                    formatted += char
            elif char == ',':
                # Peek ahead to see if the next item is '...'
                is_ellipsis = False
                for j in range(i + 1, len(code_str)):
                    if not code_str[j].isspace():
                        if code_str[j:j+3] == '...':
                            is_ellipsis = True
                        break

                # Context check: are we directly inside a dictionary?
                in_dict = (stack and stack[-1] == '{')
                current_line = formatted.split('\n')[-1]

                # Break if we are in a dict OR the line is very long, but never for ellipsis
                if (in_dict or len(current_line) > 100) and not is_ellipsis:
                    formatted += char + '\n' + (' ' * indent)
                else:
                    formatted += char + ' '
                
                # Skip following spaces
                while i + 1 < len(code_str) and code_str[i+1].isspace():
                    i += 1
            elif char == ':':
                formatted += ': '
                while i + 1 < len(code_str) and code_str[i+1].isspace():
                    i += 1
            else:
                if not char.isspace() or (formatted and not formatted[-1].isspace()):
                    formatted += char
        else:
            formatted += char
        i += 1
            
    return formatted.strip()

def format_return_value(text):
    if not text: return text
    if "```" in text: return text
    
    t_strip = text.strip()
    
    # 1. Entire text is HTML
    if t_strip.startswith('<') and t_strip.endswith('>'):
        return f"```html\n{t_strip}\n```"

    # 2. Extract balanced { ... } or [ ... ] block anywhere in the text
    start_idx = -1
    for i, char in enumerate(text):
        if char in ('{', '[', '('):
            start_idx = i
            break
            
    if start_idx != -1:
        bracket = text[start_idx]
        brackets_map = {'{': '}', '[': ']', '(': ')'}
        close_bracket = brackets_map[bracket]
        
        count = 0
        end_idx = -1
        in_string = False
        string_char = None
        
        for i in range(start_idx, len(text)):
            char = text[i]
            if char in ('"', "'") and (i == 0 or text[i-1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif string_char == char:
                    in_string = False
                    
            if not in_string:
                if char == bracket:
                    count += 1
                elif char == close_bracket:
                    count -= 1
                    if count == 0:
                        end_idx = i
                        break
                        
        if end_idx != -1:
            pre = text[:start_idx].strip()
            code = text[start_idx:end_idx+1].strip()
            post = text[end_idx+1:].strip()
            
            pretty_code = pretty_print_code(code)
            
            result = ""
            if pre: result += f"{pre}\n\n"
            result += f"```python\n{pretty_code}\n```"
            if post: result += f"\n\n{post}"
            
            return result

    # 3. Fallback
    return text

def get_regions(filepath):
    regions = []
    if not os.path.exists(filepath): return []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    stack = []
    for i, line in enumerate(lines):
        start_match = re.search(r'#\s*region\s+(.*)', line, re.IGNORECASE)
        end_match = re.search(r'#\s*endregion', line, re.IGNORECASE)
        
        if start_match:
            name = start_match.group(1).strip()
            stack.append({"name": name, "start": i + 1})
        elif end_match and stack:
            region = stack.pop()
            region["end"] = i + 1
            regions.append(region)
            
    for region in stack:
        region["end"] = len(lines)
        regions.append(region)
        
    return regions

def get_region_for_line(line, regions):
    best_region = "General"
    best_size = float('inf')
    for r in regions:
        if r["start"] <= line <= r["end"]:
            size = r["end"] - r["start"]
            if size < best_size:
                best_size = size
                best_region = r["name"]
    return best_region

def build_index():
    print("Iniciant indexació global...")
    for group, files in GROUPS.items():
        for f_path in files:
            if not os.path.exists(f_path): continue
            
            with open(f_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())
            
            regions = get_regions(f_path)
            module_name = os.path.basename(f_path).replace(".py", "")
            
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    reg_name = get_region_for_line(node.lineno, regions)
                    safe_reg = re.sub(r'[^\w\s-]', '', reg_name).strip().replace(' ', '_')
                    
                    entry = {
                        "group": group,
                        "module": module_name,
                        "region": reg_name,
                        "filename": f"{group}/{module_name}/{safe_reg}.md"
                    }
                    
                    if node.name in GLOBAL_REGISTRY:
                        print(f"WS: METODE DUPLICAT TROBAT: {node.name}")
                    
                    GLOBAL_REGISTRY[node.name] = entry
                    
                    if isinstance(node, ast.ClassDef):
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef):
                                m_reg_name = get_region_for_line(item.lineno, regions)
                                m_safe_reg = re.sub(r'[^\w\s-]', '', m_reg_name).strip().replace(' ', '_')
                                GLOBAL_REGISTRY[item.name] = {
                                    "group": group,
                                    "module": module_name,
                                    "region": m_reg_name,
                                    "filename": f"{group}/{module_name}/{m_safe_reg}.md"
                                }

def get_internal_calls(node):
    calls = set()
    for subnode in ast.walk(node):
        if isinstance(subnode, ast.Call):
            if isinstance(subnode.func, ast.Name):
                calls.add(subnode.func.id)
            elif isinstance(subnode.func, ast.Attribute):
                calls.add(subnode.func.attr)
    return calls

def generate_module_docs(filepath, group_name):
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
        tree = ast.parse(file_content)
    
    regions = get_regions(filepath)
    base_module_name = os.path.basename(filepath).replace(".py", "")
    target_dir = os.path.join(DOCS_DIR, group_name, base_module_name)
    os.makedirs(target_dir, exist_ok=True)
    
    region_content = {}

    def format_item(node, type_label, current_filename):
        doc_raw = ast.get_docstring(node)
        parsed = parse_doc(doc_raw)
        
        content = f"## `{node.name}` {{: #{node.name} }}\n"
        
        labels = get_method_labels(node)
        if labels:
            joined = " | ".join(labels)
            content += f'<small style="color: grey; display: block; margin-bottom: 15px; margin-top: -15px;">{joined}</small>\n\n'
            
        content += f"{parsed['desc']}\n\n"
        
        actual_params = get_params_list(node)
        
        content += "\n#### <i class=\"fa-solid fa-laptop-code\"></i> Exemple d'ús\n\n"
        has_ret = has_return_stmt(node) or parsed['return'] is not None
        content += generate_example_call(node.name, actual_params, is_class=isinstance(node, ast.ClassDef), has_return=has_ret)
        content += "\n\n"

        if actual_params or parsed['params']:
            content += "\n#### <i class=\"fa-solid fa-arrow-right-to-bracket\"></i> Paràmetres d'entrada\n\n"
            all_param_names = list(OrderedDict.fromkeys(actual_params + list(parsed['params'].keys())))
            for p in all_param_names:
                p_desc = parsed['params'].get(p, "-")
                content += f"- `{p}`: {p_desc}\n"
            content += "\n"
        
        if parsed['return']:
            content += f"\n#### <i class=\"fa-solid fa-arrow-right-from-bracket\"></i> Valor de retorn\n\n"
            content += f"{format_return_value(parsed['return'])}\n\n"
            
        # Cross-links
        calls = get_internal_calls(node)
        links = []
        for call in sorted(calls):
            if call in GLOBAL_REGISTRY and call != node.name:
                reg = GLOBAL_REGISTRY[call]
                # Calculate relative path
                # Documentation is in docs/Group/Module/Region.md
                # We want a link to ../../reg['group']/reg['module']/reg['filename']
                # But filename already contains group/module...
                # So from Group/Module/Region.md, we go up twice: ../../
                rel_base = "../../"
                link_path = f"{rel_base}{reg['filename']}#{call}"
                links.append(f"[`{call}`]({link_path})")
        
        if links:
            content += f"\n#### <i class=\"fa-solid fa-link\"></i> Depèn de:\n"
            content += ", ".join(links) + "\n\n"
            
        content += "\n\n---\n\n"
        return content

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if isinstance(node, ast.FunctionDef):
                reg_name = get_region_for_line(node.lineno, regions)
                safe_reg = re.sub(r'[^\w\s-]', '', reg_name).strip().replace(' ', '_')
                current_f = f"{group_name}/{base_module_name}/{safe_reg}.md"
                item_content = format_item(node, "Funció", current_f)
                
                if reg_name not in region_content:
                    region_content[reg_name] = []
                region_content[reg_name].append(item_content)
            
            elif isinstance(node, ast.ClassDef):
                # We process methods individually
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        reg_name = get_region_for_line(item.lineno, regions)
                        safe_reg = re.sub(r'[^\w\s-]', '', reg_name).strip().replace(' ', '_')
                        current_f = f"{group_name}/{base_module_name}/{safe_reg}.md"
                        
                        # Use method-specific formatting
                        parsed_m = parse_doc(ast.get_docstring(item))
                        m_content = f"### `{item.name}` {{: #{item.name} }}\n"
                        
                        m_labels = get_method_labels(item)
                        if m_labels:
                             joined = " | ".join(m_labels)
                             m_content += f'<small style="color: grey; display: block; margin-bottom: 10px; margin-top: -10px;">{joined}</small>\n\n'
                        
                        m_content += f"{parsed_m['desc']}\n\n"
                        m_params = get_params_list(item)
                        
                        m_content += "\n#### <i class=\"fa-solid fa-laptop-code\"></i> Exemple d'ús\n\n"
                        m_has_ret = has_return_stmt(item) or parsed_m['return'] is not None
                        m_content += generate_example_call(f"obj.{item.name}", m_params, has_return=m_has_ret)
                        m_content += "\n\n"

                        if m_params or parsed_m['params']:
                            m_content += "\n#### <i class=\"fa-solid fa-arrow-right-to-bracket\"></i> Paràmetres\n\n"
                            all_m_params = list(OrderedDict.fromkeys(m_params + list(parsed_m['params'].keys())))
                            for p in all_m_params:
                                p_m_desc = parsed_m['params'].get(p, "-")
                                m_content += f"- `{p}`: {p_m_desc}\n"
                            m_content += "\n"
                        
                        if parsed_m['return']:
                            m_content += f"\n#### <i class=\"fa-solid fa-arrow-right-from-bracket\"></i> Valor de retorn\n\n"
                            m_content += f"{format_return_value(parsed_m['return'])}\n\n"
                            
                        # Method cross-links
                        m_calls = get_internal_calls(item)
                        m_links = []
                        for c in sorted(m_calls):
                            if c in GLOBAL_REGISTRY and c != item.name:
                                r = GLOBAL_REGISTRY[c]
                                l_path = f"../../{r['filename']}#{c}"
                                m_links.append(f"[`{c}`]({l_path})")
                        if m_links:
                             m_content += f"\n#### <i class=\"fa-solid fa-link\"></i> Depèn de:\n"
                             m_content += ", ".join(m_links) + "\n\n"
                            
                        m_content += "\n\n---\n\n"

                        if reg_name not in region_content:
                            region_content[reg_name] = []
                        region_content[reg_name].append(m_content)

    nav_entries = []
    for region_name, lines in region_content.items():
        safe_name = re.sub(r'[^\w\s-]', '', region_name).strip().replace(' ', '_')
        filename = f"{safe_name}.md"
        with open(os.path.join(target_dir, filename), "w", encoding="utf-8") as f:
            f.write(f"# {region_name} ({base_module_name})\n\n")
            f.write("".join(lines))
        nav_entries.append({region_name: f"{group_name}/{base_module_name}/{filename}"})
        
    return nav_entries

def generate_www_md():
    www_dir = os.path.join(ROOTFS, "www")
    target_dir = os.path.join(DOCS_DIR, "WWW")
    os.makedirs(target_dir, exist_ok=True)
    index_lines = ["# Interfície Web (WWW)\n\n", "Llistat de pàgines i plantilles HTML del projecte.\n\n"]
    for file in os.listdir(www_dir):
        if file.endswith(".html"):
            index_lines.append(f"- **{file}**: Plantilla per a la vista de {file.replace('.html', '')}.\n")
    with open(os.path.join(target_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("".join(index_lines))
    return {"WWW": "WWW/index.md"}

if __name__ == "__main__":
    build_index()
    full_nav = [{"Home": "index.md"}]
    for group, files in GROUPS.items():
        group_nav = []
        for f_path in files:
            if os.path.exists(f_path):
                module_nav = generate_module_docs(f_path, group)
                base_name = os.path.basename(f_path).replace(".py", "")
                group_nav.append({base_name: module_nav})
        full_nav.append({group: group_nav})
    www_nav = generate_www_md()
    full_nav.append(www_nav)
    full_nav.append({"About": "about.md"})
    print("Documentació generada correctament!")
