from django.core.mail import send_mail


def process_call_back_data(data: dict) -> None:
    subject = "Заявка на обратную связь"
    message = (
        f"Имя: {data.get('subject')}\nТел.:{data.get('tel')}\nСсылка:{data.get('link')}"
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=["pekshev.ds@gmail.com"],
    )
