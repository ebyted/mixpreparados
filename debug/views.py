from django.http import HttpResponse

def debug_info(request):
    return HttpResponse(f"""
        <pre>
        is_secure: {request.is_secure()}
        user.is_authenticated: {request.user.is_authenticated}
        session_key: {request.session.session_key}
        HTTP_X_FORWARDED_PROTO: {request.META.get('HTTP_X_FORWARDED_PROTO')}
        </pre>
    """)