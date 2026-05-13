import os
import re
from collections import OrderedDict

ROOTFS = "C:/Users/Sira/Documents/GitHub/exitOS/exitos/rootfs"
WWW_DIR = os.path.join(ROOTFS, "www")
DOCS_DIR = "docs/WWW"

def parse_js_constants(script_content):
    """
    Busca constants globals (indentació 0-4) amb comentari a sobre.
    """
    # Regex que busca comentari + const a l'inici de línia
    pattern = r'^\s{0,4}(?:(?://\s*(.*?)\r?\n)|(?:/\*\*\s*(.*?)\s*\*/))\s*const\s+([a-zA-Z0-9_]+)\s*='
    matches = re.finditer(pattern, script_content, re.MULTILINE | re.DOTALL)
    constants = []
    for m in matches:
        comment = (m.group(1) or m.group(2) or "").strip().lstrip('*').strip()
        name = m.group(3)
        if comment:
            constants.append({"name": name, "comment": comment})
    return constants

def extract_api_calls(text):
    """Extrau els endpoints de les crides fetch()"""
    calls = re.findall(r"fetch\(['\"](.*?)['\"]", text)
    return list(OrderedDict.fromkeys(calls))

def get_api_link(endpoint):
    """Genera el link a la documentació del servidor per a un endpoint"""
    return f"../../Server/server/General.md#{endpoint}"

def parse_js_functions(script_content):
    """Parseja funcions i les seves dependències API internes"""
    pattern = r'(/\*\*.*?\*/\s*(?:async\s+)?function\s+([a-zA-Z0-9_]+)\s*\((.*?)\))'
    matches = list(re.finditer(pattern, script_content, re.DOTALL))
    
    functions = []
    for i, m in enumerate(matches):
        doc = m.group(1).split('*/')[0].strip().lstrip('/*').strip()
        name = m.group(2)
        params = [p.strip() for p in m.group(3).split(',') if p.strip()]
        
        # Determinar el cos de la funció (aproximat fins a la següent definició)
        start_pos = m.end()
        next_match_start = matches[i+1].start() if i+1 < len(matches) else len(script_content)
        body_chunk = script_content[start_pos:next_match_start]
        
        fn_api_calls = extract_api_calls(body_chunk)
        
        lines = [line.strip().lstrip('*').strip() for line in doc.split('\n')]
        desc = []
        parsed_params = {}
        ret_val = None
        
        for line in lines:
            if line.startswith('@param'):
                p_match = re.search(r'@param\s+(?:\{.*\}\s+)?([a-zA-Z0-9_]+)\s*(.*)', line)
                if p_match:
                    p_name = p_match.group(1)
                    p_desc = p_match.group(2)
                    parsed_params[p_name] = p_desc
            elif line.startswith('@return'):
                ret_val = line.replace('@return', '').strip()
            else:
                if line: desc.append(line)
        
        functions.append({
            "name": name,
            "params": params,
            "parsed_params": parsed_params,
            "desc": " ".join(desc),
            "return": ret_val,
            "api_calls": fn_api_calls
        })
    return functions

def generate_www_docs():
    os.makedirs(DOCS_DIR, exist_ok=True)
    html_files = [f for f in os.listdir(WWW_DIR) if f.endswith(".html")]
    
    print(f"Indexant {len(html_files)} fitxers HTML...")
    
    for filename in html_files:
        filepath = os.path.join(WWW_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else filename
        
        script_parts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
        script_content = "\n".join(script_parts)
        
        js_constants = parse_js_constants(script_content)
        js_functions = parse_js_functions(script_content)
        api_calls = extract_api_calls(script_content)
        html_docs = re.findall(r'<!--\s*@doc\s*(.*?):\s*(.*?)\s*-->', content)
        
        md_content = f"# {title} (`{filename}`)\n\n"
        
        # VISTA
        md_content += '=== "<i class=\\"fa-solid fa-eye\\"></i> Vista (HTML)"\n\n'
        if html_docs:
            md_content += "    #### <i class=\"fa-solid fa-layer-group\" style=\"color: #990033;\"></i> Seccions Documentades\n"
            for s_title, s_desc in html_docs:
                md_content += f"    - **{s_title}**: {s_desc}\n"
            md_content += "\n"

        ids = re.findall(r'id=["\'](.*?)["\']', content)
        unique_ids = list(OrderedDict.fromkeys(ids))
        if unique_ids:
            md_content += "    #### <i class=\"fa-solid fa-fingerprint\" style=\"color: #990033;\"></i> Elements Identificats (IDs)\n"
            for ident in unique_ids:
                if ident not in ['mainContainer', 'back-to-top-btn']:
                    md_content += f"    - `#{ident}`\n"
            md_content += "\n"
            
        # LÒGICA
        md_content += '=== "<i class=\\"fa-solid fa-brain\\"></i> Lògica (JavaScript)"\n\n'
        
        if js_constants:
            md_content += "    #### <i class=\"fa-solid fa-anchor\" style=\"color: #990033;\"></i> Constants Globals\n"
            for c in js_constants:
                md_content += f"    - **`{c['name']}`**: {c['comment']}\n"
            md_content += "\n"

        if api_calls:
            md_content += "    #### <i class=\"fa-solid fa-network-wired\" style=\"color: #990033;\"></i> Dependències API (Pàgina)\n"
            links = [f"[`{call}`]({get_api_link(call)})" for call in api_calls]
            md_content += "    " + ", ".join(links) + "\n\n"

        if js_functions:
            for fn in js_functions:
                md_content += f"    ### `{fn['name']}`\n"
                md_content += f"    {fn['desc']}\n\n"
                
                param_str = ", ".join([f"{p}=..." for p in fn['params']])
                md_content += f"    #### <i class=\"fa-solid fa-laptop-code\" style=\"color: #990033;\"></i> Exemple de crida\n\n"
                md_content += f"    ```javascript\n    {fn['name']}({param_str})\n    ```\n\n"
                
                if fn['params']:
                    md_content += f"    #### <i class=\"fa-solid fa-arrow-right-to-bracket\" style=\"color: #990033;\"></i> Paràmetres\n\n"
                    for p in fn['params']:
                        p_desc = fn['parsed_params'].get(p, "-")
                        md_content += f"    - `{p}`: {p_desc}\n"
                    md_content += "\n"
                
                if fn['api_calls']:
                    md_content += f"    #### <i class=\"fa-solid fa-link\" style=\"color: #990033;\"></i> Dependències API\n"
                    f_links = [f"[`{c}`]({get_api_link(c)})" for c in fn['api_calls']]
                    md_content += "    " + ", ".join(f_links) + "\n\n"

                if fn['return']:
                    md_content += f"    #### <i class=\"fa-solid fa-arrow-right-from-bracket\" style=\"color: #990033;\"></i> Valor de retorn\n\n"
                    md_content += f"    {fn['return']}\n\n"
                
                md_content += "    ---\n\n"
            
        target_path = os.path.join(DOCS_DIR, filename.replace(".html", ".md"))
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
    print("Documentació de la Interfície Web generada correctament!")

if __name__ == "__main__":
    generate_www_docs()
