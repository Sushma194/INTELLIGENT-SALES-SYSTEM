def stock_alert(
current_stock,
reorder_point
):

    if current_stock <= reorder_point:
        return "Reorder Required"

    return "Stock Available"