from request import Request
from authentication_middleware_handler import AuthenticationMiddleware
from authorization_middleware_handler import AuthorizationMiddleware
from security_checks_middleware_handler import SecurityChecksMiddleware
from request_processor import RequestProcessor


def main():
    # Create the request with authentication, authorization, and security check flags
    request = Request(
        request_type="SomeRequest",
        is_authenticated=True,  # Change these to test different scenarios
        is_authorized=True,
        has_passed_security_checks=True
    )

    # Create middleware handlers
    auth_middleware = AuthenticationMiddleware()
    authorization_middleware = AuthorizationMiddleware()
    security_middleware = SecurityChecksMiddleware()

    # Set up the chain of responsibility
    auth_middleware.set_next(authorization_middleware).set_next(security_middleware)

    # Create the request processor with the middleware chain
    request_processor = RequestProcessor(auth_middleware)

    # Process the request
    response = request_processor.process_request(request)

    # Print the response
    print(f"Response: {response.get_reason()}, Success: {response.is_succeeded()}")

if __name__ == "__main__":
    main()
