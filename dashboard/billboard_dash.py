# Importación de librerías necesarias para el desarrollo del dashboard
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Dash, callback, Input, Output

# Carga de datos desde archivos CSV
# Cada archivo contiene un ranking musical diferente.
hot100 = pd.read_csv("datasets/hot100.csv")
global200 = pd.read_csv("datasets/global200.csv")
billboard200 = pd.read_csv("datasets/billboard200.csv")
tiktok50 = pd.read_csv("datasets/tiktok50.csv")

# Función para generar un gráfico de barras con los datos de "hot100"
def grafica_barras():
    # Se representa el peak (posición máxima alcanzada) de cada canción en el ranking
    fig_bar = px.bar(
        hot100,
        x="SongName", # Canción en el eje X
        y="Peak", # Posición máxima alcanzada en el eje Y
        title="Peak de Canciones en el Billboard Hot 100",
        labels={"SongName": "Canción", "Peak": "Posición Máxima"},
        template="plotly_dark"
    )
    fig_bar.update_xaxes(tickangle=45, title="Canciones")  # Inclina las etiquetas de las canciones
    fig_bar.update_yaxes(title="Posición Máxima (Peak)")
    return fig_bar
# Función para generar un gráfico de dispersión con los datos de "hot100"
def grafica_dispersion():
    # Representa las canciones por artista, mostrando su peak y semanas en la lista
    fig_scatter = px.scatter(
        hot100,
        x="Artist",  # Artistas en el eje X
        y="Peak",  # Posición máxima alcanzada en el eje Y
        color="SongName",  # Color según el nombre de la canción
        size="Weeks",  # Tamaño del punto según semanas en la lista
        title="Peak de Canciones por Artista",
        labels={"Artist": "Artista", "Peak": "Posición Máxima"},
        template="plotly_dark",  # Estilo visual oscuro
        hover_data=["SongName"],  # Información adicional al pasar el cursor
        height=750  # Altura del gráfico
    )
    fig_scatter.update_yaxes(autorange="reversed")  # El mejor peak es 1, así que lo invertimos
    return fig_scatter

# Función principal que estructura el contenido del dashboard
def dashboard():
    fig_bar = grafica_barras()  # Genera gráfico de barras
    fig_scatter = grafica_dispersion()  # Genera gráfico de dispersión

    # Diseño del cuerpo principal del dashboard
    body = html.Div(
        [
            dbc.Row(
                [
                    # Columna izquierda: Filtros
                    dbc.Col(
                        html.Div([
                            html.H3("Filtros", style={"color": "white"}),  # Título
                            html.Hr(),  # Línea divisoria
                            tarjeta_filtro(),  # Componente de filtro
                        ], style={  # Estilo de la tarjeta de filtros
                            "background-color": "rgba(0, 0, 0, 0.8)",  # Fondo semitransparente
                            "padding": "20px",
                            "border-radius": "10px",
                        }), width=4
                    ),
                    # Columna derecha: Gráficos
                    dbc.Col(
                        html.Div([
                            dbc.Row(dcc.Graph(figure=fig_bar, id="figLine", style={"margin-bottom": "10px"})),
                            # Gráfico de barras
                            dbc.Row(dcc.Graph(figure=fig_scatter, id="figScatter"))  # Gráfico de dispersión
                        ]), width=10
                    )
                ]
            )
        ],
        style={  # Estilo del fondo principal
            "background-color": "#000000",  # Fondo negro
            "background-image": "url('/assets/f0a05304782a00d680225ca28886fbb621-MusicColorEras.rhorizontal.w610.gif')",
            # Imagen de fondo
            "background-size": "cover",  # Cubrir todo el espacio
            "background-position": "center",  # Centrar imagen
            "background-attachment": "fixed",  # Imagen fija
        }
    )
    return body

# Tarjeta que contiene el dropdown para seleccionar datasets
def tarjeta_filtro():
    control = dbc.Card(
        [
            html.Div([
                dcc.Dropdown(
                    id="graph-type-dropdown", # ID del dropdown
                    options=[
                        {"label": "HOT100", "value": "hot100"},
                        {"label": "GLOBAL200", "value": "global200"},
                        {"label": "BILLBOARD200", "value": "billboard200"},
                        {"label": "TIKTOK50", "value": "tiktok50"}
                    ],
                    value="hot100"  # Selección por defecto
                )
            ])
        ]
    )
    return control

# Layout principal con navegación
def menu_dashboard():
    # Barra lateral
    sidebar = html.Div(
        [
            # Logo centrado en la parte superior del sidebar
            html.Div(
                html.Img(src="/assets/Billboard_Logo_2013.svg.png", style={"max-width": "100%", "height": "auto"}),
                style={
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "flex-start",
                    "margin-top": "20px",
                    "margin-bottom": "30px",
                }
            ),
            html.Hr(),
            html.P("Menu:", className="lead", style={"color": "black", "text-align": "center"}),
            dbc.Nav(
                [ # Links de navegación
                    dbc.NavLink("Home",
                                href="/",
                                active="exact",
                                style={"color": "white", "font-weight": "bold", "background-color": "black"}),
                    dbc.NavLink("Dashboards",
                                href="/dash-1",
                                active="exact",
                                style={"color": "white", "font-weight": "bold", "background-color": "black"}),
                ],
                vertical=True,
                pills=True,
                style={"background-color": "white"}
            ),
            # Espacio adicional para la imagen
            html.Div(
                html.Img(
                    src="/assets/91JfYzFvjxL.jpg",  # Cambia esta ruta a la de tu imagen
                    style={
                        "width": "100%",  # Ocupa todo el ancho del contenedor
                        "height": "100%",  # Ajusta al espacio disponible
                        "object-fit": "cover",  # Escala la imagen sin distorsión
                        "margin-top": "10px",  # Separación opcional
                    },
                ),
                style={
                    "flex-grow": "1",  # Ocupa el espacio restante en el contenedor
                    "overflow": "hidden",  # Previene que la imagen se salga del contenedor
                },
            ),
        ],
        style={
            "background-color": "white",
            "color": "black",
            "height": "100vh",
            "padding": "10px",
            "width": "250px",
            "display": "flex",
            "flex-direction": "column",  # Asegura que los elementos estén en columna
        },
    )

    # Contenido principal
    content = html.Div(
        id="page-content",
        style={
            "position": "relative",  # Hace que el contenido sea relativo
            "background-color": "white",
            "flex-grow": "1",
            "overflow": "hidden",  # Evita el scroll si hay desbordamiento
        }
    )

    # Contenedor principal
    return html.Div(
        [
            dcc.Location(id="url"),
            sidebar,
            content,  # Contenido dinámico del dashboard
        ],
        style={
            "display": "flex",
            "min-height": "100vh",
        }
    )

# Callback para actualizar gráficos en función del archivo seleccionado
@callback(
    Output(component_id="figLine", component_property="figure"),
    Output(component_id="figScatter", component_property="figure"),
    Input(component_id="graph-type-dropdown", component_property="value")
)
def update_graph(selected_dataset):
    # Selección del dataset
    if selected_dataset == "hot100":
        dataset = hot100
    elif selected_dataset == "global200":
        dataset = global200
    elif selected_dataset == "billboard200":
        dataset = billboard200
    elif selected_dataset == "tiktok50":
        dataset = tiktok50
    else:
        # Si no se selecciona nada, devolver gráficos vacíos
        return {}, {}

    # Gráfico de barras
    fig_bar = px.bar(
        dataset,
        x="SongName",
        y="Peak",
        title=f"Peak de Canciones - {selected_dataset.upper()}",
        labels={"SongName": "Canción", "Peak": "Posición Máxima"},
        template="plotly_dark"
    )
    fig_bar.update_xaxes(tickangle=45, title="Canciones")
    fig_bar.update_yaxes(title="Posición Máxima (Peak)")

    # Gráfico de dispersión
    fig_scatter = px.scatter(
        dataset,
        x="Artist",
        y="Peak",
        color="SongName",
        size="Weeks",
        title=f"Peak por Artista - {selected_dataset.upper()}",
        labels={"Artist": "Artista", "Peak": "Posición Máxima", "Weeks": "Semanas"},
        template="plotly_dark",
        hover_data=["SongName"]
    )
    fig_scatter.update_yaxes(autorange="reversed")  # El mejor peak es 1, así que lo invertimos

    return fig_bar, fig_scatter

# Callback para actualizar el contenido según la navegación
@callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def render_page_content(pathname):
    # Ruta de la imagen JPG (asegúrate de que la ruta sea correcta)
    background_image = "/assets/TikDownloader.io_7388784597720550661_hd.mov"  # Cambia esto por la ruta correcta de tu video

    if pathname == "/":
        return html.Div(
            [html.H1(".")],
            style={
                "background-image": f"url({background_image})",  # Establece la imagen de fondo
                "background-size": "cover",  # Asegura que la imagen cubra toda el área
                "background-position": "center",  # Centra la imagen en el fondo
                "background-repeat": "no-repeat",  # Evita que la imagen se repita
                "height": "100vh",  # Hace que la imagen cubra toda la altura de la página
                "color": "white",  # Color del texto blanco para que contraste con la imagen de fondo
                "text-align": "center",  # Centra el texto horizontalmente
                "display": "flex",  # Usamos flexbox para centrar el contenido
                "justify-content": "center",  # Centra el contenido verticalmente
                "align-items": "center",  # Centra el contenido verticalmente
            },
        )
    elif pathname == "/dash-1":
        return dashboard()

    # Si la ruta no se reconoce, mostrar un 404 con la imagen de fondo
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        style={
            "background-image": f"url({background_image})",  # Establece la imagen de fondo
            "background-size": "cover",  # Asegura que la imagen cubra toda el área
            "background-position": "center",  # Centra la imagen en el fondo
            "background-repeat": "no-repeat",  # Evita que la imagen se repita
            "height": "100vh",  # Hace que la imagen cubra toda la altura de la página
            "color": "white",  # Texto blanco para que contraste con la imagen
            "text-align": "center",  # Centra el texto horizontalmente
            "display": "flex",  # Usamos flexbox para centrar el contenido
            "justify-content": "center",  # Centra el contenido verticalmente
            "align-items": "center",  # Centra el contenido verticalmente
        },
    )

if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH], suppress_callback_exceptions=True) # Instancia de la aplicación
    app.layout = menu_dashboard()  # Define el layout
    app.run(debug=True)  # Modo debug activado
