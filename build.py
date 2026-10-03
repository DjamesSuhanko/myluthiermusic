#!/usr/bin/env python3
"""Small static site. Only dist/ is published; application/customer files stay outside."""
from pathlib import Path
from string import Template
import html, os, re, shutil
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'dist'
BASE=os.environ.get('BASE_PATH','').rstrip('/')
if BASE and (not BASE.startswith('/') or '..' in BASE or any(c in BASE for c in '<>"\'')):
    raise ValueError('BASE_PATH must be an absolute URL path')

def prose(source):
    def inline(text):
        text=html.escape(text)
        text=re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',text)
        return text.replace('djames.suhanko@gmail.com','<a href="mailto:djames.suhanko@gmail.com">djames.suhanko@gmail.com</a>')
    result=[]
    for block in source.strip().split('\n\n'):
        if block.startswith('# '):result.append('<h1>'+inline(block[2:])+'</h1>')
        elif block.startswith('## '):result.append('<h2>'+inline(block[3:])+'</h2>')
        elif block.startswith('- '):result.append('<ul>'+''.join('<li>'+inline(line[2:])+'</li>' for line in block.splitlines())+'</ul>')
        else:result.append('<p>'+inline(block)+'</p>')
    return '\n'.join(result)

def build():
    if OUT.exists():shutil.rmtree(OUT)
    OUT.mkdir();shutil.copytree(ROOT/'assets',OUT/'assets')
    shutil.copyfile(ROOT/'CNAME',OUT/'CNAME');(OUT/'.nojekyll').touch()
    template=Template((ROOT/'templates/base.html').read_text())
    privacy='<article class="article"><div class="breadcrumbs"><a href="'+BASE+'/">MyLuthier</a> / Privacidade</div>'+prose((ROOT/'content/privacy.md').read_text())+'</article>'
    contact='''<article class="article contact"><p class="eyebrow">MyLuthier · Clave Sol</p><h1>Contato</h1><p>Dúvidas sobre o aplicativo ou solicitações relacionadas à privacidade:</p><h2>Djames Suhanko</h2><p><a class="contact-mail" href="mailto:djames.suhanko@gmail.com">djames.suhanko@gmail.com</a></p><p class="note">Medições e relatórios ficam no seu dispositivo. Envie somente as informações necessárias ao atendimento.</p></article>'''
    pages=[('/', 'MyLuthier','Informações públicas do aplicativo MyLuthier.',Template((ROOT/'content/index.html').read_text()).substitute(base=BASE),True),
           ('/privacidade/','Política de Privacidade','Como o MyLuthier utiliza o microfone, armazena relatórios e permite excluir dados.',privacy,False),
           ('/contato/','Contato','Contato do desenvolvedor e atendimento de privacidade do MyLuthier.',contact,False),
           ('/404.html','Página não encontrada','Página não encontrada no MyLuthier.','<article class="article contact"><p class="eyebrow">404</p><h1>Página não encontrada</h1><p><a href="'+BASE+'/">Voltar ao MyLuthier</a></p></article>',True)]
    for path,title,description,body,noindex in pages:
        navigation=''.join('<a href="'+BASE+url+'"'+(' aria-current="page"' if url==path else '')+'>'+label+'</a>' for url,label in [('/','MyLuthier'),('/privacidade/','Privacidade'),('/contato/','Contato')])
        rendered=template.substitute(title=html.escape(title),description=html.escape(description),base=BASE,canonical=path,
            robots='<meta name="robots" content="noindex,follow">' if noindex else '',navigation=navigation,body=body)
        output=OUT/(path.lstrip('/')+('index.html' if path.endswith('/') else ''));output.parent.mkdir(parents=True,exist_ok=True);output.write_text(rendered)
    # Preserve a simple HTML address usable in Play Console too.
    (OUT/'privacy.html').write_text((OUT/'privacidade/index.html').read_text())
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n')
    print('Site gerado em',OUT)
if __name__=='__main__':build()
