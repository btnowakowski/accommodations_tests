from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceData:
    """
    A data class representing service information.

    Attributes:
        name: The name of the service.
        description: A description of the service.
        price: Service price
        duration: Slot duration in minutes
        services_link: Navigation link text to services page
        services_link_role: Navigation link element role
    """

    name: str = "Test Service"
    description: str = "Service for testing purposes"
    price: str = "50"
    duration: str = "90"
    services_link: str = "Usługi"
    services_link_role: str = "link"


TEST_SERVICE: ServiceData = ServiceData()
