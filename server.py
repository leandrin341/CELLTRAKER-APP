import http.server
import socketserver
import webbrowser
import os

PORT = 3000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"================================================================")
    print(f"  UroScan AI - Hospital Italiano (Servicio de Urologia)")
    print(f"  Servidor iniciado en: http://localhost:{PORT}")
    print(f"  Presiona Ctrl+C para detener el servidor")
    print(f"================================================================")
    
    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")
