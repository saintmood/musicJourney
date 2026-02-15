import graphviz
import os

# On Gentoo ensure graphviz is installed:
# sudo emerge media-gfx/graphviz
# pip install graphviz


def create_music_map():
    # Create directed graph
    dot = graphviz.Digraph('My Music Journey',
                           comment='Music Discovery Path')

    # --- Style Configuration (Engineering Blueprint Look) ---
    dot.attr(rankdir='LR')  # Left to Right (Timeline)
    dot.attr(bgcolor='#ffffff')
    dot.attr(splines='ortho')  # Orthogonal lines
    dot.attr(nodesep='0.6', ranksep='0.8')

    # Default node styles
    dot.attr('node', shape='box', style='rounded,filled',
             fontname='Sans', fontsize='10', penwidth='1.5')
    dot.attr('edge', fontname='Sans', fontsize='9', color='#555555')

    # --- Status Legend (Helper Function) ---
    def add_node(id, label, status='backlog', note=None):
        """
        status:
          'done' (Green) - Listened & Liked
          'current' (Blue) - Currently listening
          'next' (Yellow) - Next in queue
          'rejected' (Red) - Did not like
        """
        colors = {
            'done': ('#e6fffa', '#2c7a7b'),      # Mint background, Teal border
            'current': ('#ebf8ff', '#2b6cb0'),   # Blue
            'next': ('#fffaf0', '#dd6b20'),      # Orange/Yellow
            'rejected': ('#fff5f5', '#c53030'),  # Red
            'backlog': ('#f7fafc', '#a0aec0')    # Grey
        }

        bg_color, border_color = colors.get(status, colors['backlog'])

        # HTML-like label for formatting
        if note:
            html_label = f'<{
                label}<BR/><FONT POINT-SIZE="8" COLOR="#555555"><I>{note}</I></FONT>>'
        else:
            html_label = f'<{label}>'

        dot.node(id, html_label, fillcolor=bg_color, color=border_color)

    # ==========================================
    # YOUR HISTORY (DATA SECTION)
    # ==========================================

    # 2. Conscious Blues-Rock (Entry Point)
    add_node('Derek', 'Derek And The Dominos', status='done',
             note='Layla Album. The Entry Point')

    # 3. Excavating Clapton
    add_node('Clapton', 'Eric Clapton (Solo)', status='done', note='The Roots')
    add_node('Mayall', 'John Mayall And The Bluesbreakers',
             status='done', note='The Beano Album. Talent Incubator')

    # 4. Power Trio
    add_node('Cream', 'Cream', status='done', note='Heavy Psychedelic Blues')

    # 5. Branches
    add_node('BlindFaith', 'Blind Faith', status='done',
             note='Steve Winwood carries the load')

    # 7. FUTURE (Next Station)
    add_node('PeterGreen', 'Fleetwood Mac (Early)', status='next',
             note='Album "The Pious Bird..."\nTrack "Albatross"')
    add_node('Allman', 'Allman Brothers Band', status='backlog',
             note='Duane Allman (Slide Guitar)')

    # ==========================================
    # CONNECTIONS (LOGIC SECTION)
    # ==========================================

    # Logic flow
    dot.edge('Derek', 'Clapton', label='Who is the guitarist?')
    dot.edge('Clapton', 'Mayall', label='Where did he come from?')
    dot.edge('Mayall', 'Cream', label='Where did Eric go?')

    dot.edge('Cream', 'BlindFaith', label='What after the breakup?')

    # Recommendation Branch (Current Path)
    dot.edge('Mayall', 'PeterGreen', label='Who replaced Eric?',
             color='#dd6b20', style='dashed', penwidth='2.0')

    # Link Layla -> Allman (Future Reference)
    dot.edge('Derek', 'Allman', label='Who is the 2nd guitarist?', style='dotted')

    # Rendering
    output_path = 'music_journey'
    try:
        dot.render(output_path, view=False, format='png')
        print(f"Map updated: {os.getcwd()}/{output_path}.png")
    except Exception as e:
        print(f"Error rendering graph: {e}")
        print("Ensure graphviz is installed: sudo emerge media-gfx/graphviz")


if __name__ == '__main__':
    create_music_map()
