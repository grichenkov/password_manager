import json
from typing import Any
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.docs import swagger_ui_default_parameters
from starlette.responses import HTMLResponse


def get_swagger_ui_html(
    *,
    openapi_url: str = "/openapi.json",
    title: str = "Password Manager",
    swagger_js_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
    swagger_css_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css",
    swagger_ui_parameters: dict[str, Any] | None = None,
) -> HTMLResponse:
    """Метод для генерации кастомного HTML Swagger UI."""
    current_swagger_ui_parameters = swagger_ui_default_parameters.copy()
    if swagger_ui_parameters:
        current_swagger_ui_parameters.update(swagger_ui_parameters)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="{swagger_css_url}">
    <title>{title}</title>
    </head>
    <body>
    <div id="swagger-ui"></div>
    <script src="{swagger_js_url}"></script>
    <script>
    const ui = SwaggerUIBundle({{
        url: '{openapi_url}',
        dom_id: "#swagger-ui",
    """

    for key, value in current_swagger_ui_parameters.items():
        html += f"{json.dumps(key)}: {json.dumps(jsonable_encoder(value))},\n"

    html += """
    presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
    })
    </script>
    </body>
    </html>
    """
    return HTMLResponse(html)
