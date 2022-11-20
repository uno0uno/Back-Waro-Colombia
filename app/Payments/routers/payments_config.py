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
                "title": payments.title,
                "quantity": payments.quantity,
                "unit_price": payments.unit_price,
            }
        ]
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return preference

