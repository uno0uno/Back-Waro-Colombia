#ENV MELINA_SDK
from app.config.config import MELINA_SDK

# SDK de Mercado Pago
import mercadopago

# Agrega credenciales
sdk = mercadopago.SDK(MELINA_SDK)

#Models app Waro Colombia(Internal-post)
from app.models.models import Payments

# =============================================
# Payment Pathner
# =============================================
def preference_data_merlina(payments:Payments):
    # Crea un ítem en la preferencia
    preference_data = {
        "items": [
            {
                "id": "p1",
                "title": payments.title,
                "currency_id": payments.currency_id,
                "description": payments.description,
                "quantity": payments.quantity,
                "unit_price": payments.unit_price,
            }
        ],
        "back_urls": 
            {
            "success": "http://127.0.0.1:5173/#/parthner/"+payments.email+"/bill",
            "failure": "http://127.0.0.1:5173/#/parthner/"+payments.email+"/bill",
            "pending": "http://127.0.0.1:5173/#/parthner/"+payments.email+"/bill"
            },
        "auto_return": "approved",
        "statement_descriptor": "Waro Colombia"
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return preference

