def individual_serial(ticket) -> dict:
    return {
        "id": str(ticket["_id"]),
        "title": ticket.get("title", "No Title"),
        "description": ticket.get("description", "No Description"),
        "category": ticket.get("category", "No Category"),
        "priority": ticket.get("priority", "No Priority"),
        "progress": ticket.get("progress", "No Progress"),
        "status": ticket.get("status", "No Status"),
        "active": ticket.get("active", False),
    }


def list_serial(tickets) -> list:
    return [individual_serial(ticket) for ticket in tickets]
