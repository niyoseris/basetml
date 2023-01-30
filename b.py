import base64

def file_to_base64(filepath):
    with open(filepath, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
    return encoded_string

def create_html(filepath, aligment, title):
    encoded_string = file_to_base64(filepath)
    if filepath.endswith(".mp4"):
        html = f"""
        <html>
        <head>
        <title>{title}</title>
        </head>
        <body>
        <center>
        <h1 style="text-align:{aligment}">{title}</h1>
        <video controls width="800" style="text-align:{aligment}">
        <source src="data:video/mp4;base64,{encoded_string}" type="video/mp4">
        Your browser does not support the video tag.
        </video>
        </center>
        </body>
        </html>
        """
    else:
        html = f"""
        <html>
        <head>
        <title>{title}</title>
        </head>
        <body>
        <center>
        <h1 style="text-align:{aligment}">{title}</h1>
        <img src="data:image/png;base64,{encoded_string}" alt="{title}" style="text-align:{aligment}">
        </center>
        </body>
        </html>
        """
    return html

def write_html(filepath, aligment, title):
    html = create_html(filepath, aligment, title)
    with open(f"{filepath}.html", "w") as file:
        file.write(html)

if __name__ == "__main__":
    filepath = input("Enter the file path: ")
    aligment = input("Enter the aligment (left, center, right): ")
    title = input("Enter the title: ")
    write_html(filepath, aligment, title)
