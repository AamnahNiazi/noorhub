import reflex as rx

config = rx.Config(
    app_name="noorhub",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)