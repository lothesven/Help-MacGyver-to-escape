"""functions to manage text based issues"""

def blit_text(surface, text, position, font, color):
    """Blit text inside a surface going to next line if text is too long.
    Does not avoid too long text to exceed surface height"""
    words = [word.split(' ') for word in text.splitlines()]
    # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width = surface.get_width()
    x_pos, y_pos = position
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x_pos + word_width >= max_width:
                x_pos = position[0]  # Reset the x.
                y_pos += word_height  # Start on new row.
            surface.blit(word_surface, (x_pos, y_pos))
            x_pos += word_width + space
        x_pos = position[0]  # Reset the x.
        y_pos += word_height  # Start on new row.
