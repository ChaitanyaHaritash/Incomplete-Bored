import json
import cherrypy

def load_messages(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        return json.load(file)

class MessageServer:
    @cherrypy.expose
    def index(self):
        messages = load_messages("flexible_chat_data.json")  
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Translated Messages</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
                table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Translated Messages</h1>
            <table>
                <tr>
                    <th>Timestamp</th>
                    <th>Sender</th>
                    <th>Message</th>
                </tr>
        """
        for entry in messages:

            html_content += f"""
                <tr>
                    <td>{entry.get("timestamp", "")}</td>
                    <td>{entry.get("sender_alias", "")}</td>
                    <td>{entry.get("message", "")}</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        return html_content

if __name__ == "__main__":
    cherrypy.config.update({'server.socket_port': 8080})  # Runs on http://127.0.0.1:8080
    cherrypy.quickstart(MessageServer())