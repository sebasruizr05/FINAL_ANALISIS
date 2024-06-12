from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def submit_form(self):
        # Datos del formulario a enviar
        form_data = {
            "name": "John Sebastian",
            "email": "johnville@gmail.com",
            "message": "Hola, la buena Juanca!"
        }

        # Enviar una solicitud POST al endpoint de contacto con los datos del formulario
        self.client.post("/contact", data=form_data)


