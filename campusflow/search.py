
def validate_title(title):
    if not isinstance(title, str):
        raise TypeError("invalid title: title must be string")
    cleaned_title = title.strip().casefold() 
    if cleaned_title == "":
        raise ValueError("Ticket title cannot be blank")
    
    return cleaned_title

def validate_category(category):
    if not isinstance(category, str):
        raise TypeError("invalid category: category must be string")
    cleaned_category = category.strip().casefold() 
    if cleaned_category == "":
        raise ValueError("Ticket title cannot be blank")
    if cleaned_category not in ["Network", "Hardware", "Software"]:
        raise ValueError("ticket category must be Network, Hardware, or Software")
    
    return cleaned_category

def validate_status(status):
    if not isinstance(status, str):
        raise TypeError("invalid category: category must be string")
    cleaned_status = status.strip().casefold() 
    if cleaned_status == "":
        raise ValueError("Ticket status cannot be blank")
    if cleaned_status not in ["Open", "in_progress", "Resolved" "Closed"]:
        raise ValueError("ticket category must be Open, In_progress, Resolved, or Closed")
    
    return cleaned_status

def validate_priority(priority):
    if not isinstance(priority, str):
        raise TypeError("invalid category: category must be string")
    cleaned_priority = priority.strip().casefold() 
    if cleaned_priority == "":
        raise ValueError("Ticket priority cannot be blank")
    if cleaned_priority not in ["critical", "high", "medium" "low"]:
        raise ValueError("ticket priority must be critical, high, medium, or low")
    
    return cleaned_priority

def extract_ticket_number(ticket_id):
    if isinstance(ticket_id, str):
        digits = "".join(ch for ch in ticket_id if ch.isdigit())
        if digits:
            return int(digits)
    return float('inf')

PRIORITY_RANK = {
    "critical": 1,
    "high": 2,
    "medium": 3,
    "low": 4
}

def search_tickets(
    tickets,
    title,
    category,
    status,
    priority,
    sort_results
):
    if not isinstance(tickets, dict):
        raise TypeError("tickets must be a dictionary")
    
    cleaned_title = validate_title(title)
    cleaned_category = validate_category(category)
    cleaned_status = validate_status(status)
    cleaned_priority = validate_priority(priority)

    matches = []

    for ticket in tickets:
        if cleaned_title is not None:
            ticket_title = str(ticket.get("title", "")).casefold()
            if cleaned_title not in ticket_title:
                continue

        if cleaned_category is not None:
            ticket_cat = str(ticket.get("category", "")).casefold()
            if ticket_cat != cleaned_category:
                continue

        if cleaned_status is not None:
            ticket_status = str(ticket.get("status", "")).casefold()
            if ticket_status != cleaned_status:
                continue

        if cleaned_priority is not None:
            ticket_priority = str(ticket.get("priority", "")).casefold()
            if ticket_priority != cleaned_priority:
                continue

        matches.append(ticket)

    if sort_results:
        def sort_key(t):
            rank = PRIORITY_RANK.get(str(t.get("priority", "")).lower(), 99)
            num_id = extract_ticket_number(t.get("id", ""))
            return (rank, num_id)

        return sorted(matches, key=sort_key)

    return list(matches)

