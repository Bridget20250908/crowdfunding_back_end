from django.conf import settings
from django.http import HttpResponse, Http404
import os

try:
    import markdown as md
except Exception:
    md = None


def readme(request):
    """Render the project's `README.md` to HTML with images served from STATIC_URL.

    The view rewrites relative image links in the Markdown to point to
    `settings.STATIC_URL` so images located in the app's `static/` directory
    are served correctly after `collectstatic`.
    """
    readme_path = os.path.join(settings.BASE_DIR, 'static/README.md')
    try:
        with open(readme_path, 'r', encoding='utf-8') as fh:
            content = fh.read()
    except FileNotFoundError:
        raise Http404('README.md not found')

    # rewrite relative image links: ![alt](filename.png) -> ![alt](/static/filename.png)
    try:
        import re

        def _rewrite_image(match):
            alt = match.group(1)
            src = match.group(2).strip()
            # keep absolute URLs and root-relative URLs intact
            if src.startswith('http://') or src.startswith('https://') or src.startswith('/'):
                return match.group(0)
            return f"![{alt}]({settings.STATIC_URL}{src})"

        content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', _rewrite_image, content)
    except Exception:
        pass

    if md is None:
        # fallback to raw markdown if Markdown isn't available
        return HttpResponse(content, content_type='text/markdown')

    html_body = md.markdown(content, extensions=['fenced_code', 'tables'])

    # Use GitHub Markdown CSS from a CDN for GitHub-like styling. We also add
    # a small local override to ensure images and code blocks behave nicely.
    html = f"""<!doctype html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <title>README</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css" integrity="" crossorigin="anonymous">
        <style>
            .markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }}
            img {{ max-width: 100%; height: auto; }}
            pre {{ overflow: auto; }}
            @media (max-width: 767px) {{ .markdown-body {{ padding: 15px; }} }}
        </style>
    </head>
    <body>
        <article class="markdown-body">{html_body}</article>
    </body>
</html>"""

    return HttpResponse(html, content_type='text/html')
