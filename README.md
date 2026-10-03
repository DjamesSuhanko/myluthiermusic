# MyLuthier · páginas públicas Clave Sol

Site independente do código do aplicativo, preparado para **myluthier.clavesol.com.br**. A identidade utiliza o fundo claro, verde, dourado, DM Sans, Playfair Display e a marca do Clave Sol. O logo do MyLuthier é o PNG fornecido pelo proprietário, mantido sem alterações.

## Conteúdo

- `content/index.html`: index provisório; aguarda o conteúdo definitivo do proprietário. Está com `noindex,follow` até essa troca.
- `content/privacy.md`: política de privacidade do aplicativo, copiada de MyLuthierAndroid/docs/privacy.md. Manter as cópias sincronizadas quando o tratamento dos dados mudar.
- `/privacidade/` e `/privacy.html`: versões públicas da política, com o mesmo texto.
- `/contato/`: canal de atendimento existente do desenvolvedor.
- `templates/base.html` e `assets/style.css`: identidade comum de todas as páginas.

Não há anúncios, analytics, formulários de coleta ou JavaScript. Como no Clave Sol, as fontes são carregadas do Google Fonts, que recebe as requisições normais do navegador; isso diz respeito ao site, não ao funcionamento offline do aplicativo.

## Prévia local

```bash
python3 build.py
python3 scripts/check_site.py
python3 -m http.server 8080 --directory dist
```

Abra http://localhost:8080. Não publique a raiz do repositório; publique somente `dist/`.

## Publicação futura

O arquivo `CNAME` já contém `myluthier.clavesol.com.br`. Os arquivos estáticos prontos para hospedagem estão em `dist/`. O proprietário ainda criará o subdomínio e configurará o domínio customizado nas opções do Pages. A preparação local não altera DNS, não habilita Pages e não publica nada por conta própria.

Quando o conteúdo do index chegar, substituir `content/index.html`, atualizar a descrição correspondente em `build.py` e retirar apenas o `noindex` da página inicial. As páginas de privacidade e contato permanecem disponíveis separadamente. Nenhum link de loja ou alegação promocional provisória foi inventado.

URL prevista para o Play Console, depois de o site estar publicado: https://myluthier.clavesol.com.br/privacidade/
