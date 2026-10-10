# Editar o conteúdo do site

Edite os arquivos da pasta `content/`:

- `index.md`: apresentação, capa e blocos da página inicial.
- `privacy.md`: política de privacidade.
- `contact.md`: contato.

Não edite `dist/`: ela é recriada pelo build. Os templates HTML cuidam somente da apresentação visual.

## Página inicial

O início de `index.md` contém três campos, seguidos de uma linha vazia:

```markdown
Title: Nome do aplicativo
Description: Uma descrição curta do aplicativo.
Image: nome-da-capa.webp

Um parágrafo opcional sobre o app.

## Recursos

- Primeiro recurso.
- Segundo recurso.

[Conhecer mais](https://exemplo.com/)
```

`Image` é o nome/caminho dentro de `assets/`. Cada seção iniciada por `##` vira um bloco da apresentação. Não use `#` no corpo da página inicial: o título principal vem de `Title`.

## Formatação e imagens

Use `**negrito**`, `*itálico*`, listas, links e tabelas Markdown. Guarde imagens em `assets/` e insira:

```markdown
![Descrição da imagem]({{BASE}}/assets/minha-imagem.webp)
```

Use `{{BASE}}/contato/` e `{{BASE}}/privacidade/` para links internos. O gerador ajusta a base do endereço. Na política e no contato, mantenha exatamente um título `#`; subseções usam `##`.

## Conferir e publicar

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python build.py
python -m http.server 8000 --directory dist
```

Abra http://localhost:8000. Se houver `scripts/check_site.py`, execute `python scripts/check_site.py` para verificar os links locais. Depois de revisar, faça commit e push; o workflow instala Markdown e publica normalmente. A URL `/privacidade/` e o alias `/privacy.html` continuam iguais.
