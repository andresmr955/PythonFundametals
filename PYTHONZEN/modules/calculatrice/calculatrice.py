from figures import area_circle, area_rectangle

def calculate_area(figure, *args):
    """
    Calculate the area of a given figure.
    
    Parameters:
    figure (str): The type of figure ('circle' or 'rectangle').
    *args: The dimensions of the figure.
    
    Returns:
    float: The area of the figure.
    
    Raises:
    ValueError: If the figure type is not recognized or if the arguments are invalid.
    """
    if figure == "circle":
        if len(args) != 1 or args[0] <= 0:
            raise ValueError("Invalid arguments for circle. Expected one positive radius.")
        return area_circle(args[0])
    
    elif figure == "rectangle":
        if len(args) != 2 or any(arg <= 0 for arg in args):
            raise ValueError("Invalid arguments for rectangle. Expected two positive dimensions.")
        return area_rectangle(*args)
    
    else:
        raise ValueError(f"Figure '{figure}' is not recognized. Use 'circle' or 'rectangle'.")