from django.core.mail import send_mail
from index_app.models import ContactInfo


def process_call_back_data(data: dict) -> None:
    subject = "Заявка на обратную связь"
    message = (
        f"Имя: {data.get('subject')}\nТел.:{data.get('tel')}\nСсылка:{data.get('link')}"
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        # recipient_list=["cidercity@yandex.ru"],
        recipient_list=[item.value for item in ContactInfo.available_emails.all()],
    )
