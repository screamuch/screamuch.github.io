#!/usr/bin/env python3
"""Generate the Music AI pipeline diagram as SVG"""

def generate_pipeline_svg(output_path):
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append('<svg width="900" height="460" xmlns="http://www.w3.org/2000/svg">')

    # Background
    svg.append('  <rect width="900" height="460" fill="#ffffff"/>')

    # Arrow marker definition
    svg.append('  <defs>')
    svg.append('    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">')
    svg.append('      <polygon points="0 0, 10 3.5, 0 7" fill="#000"/>')
    svg.append('    </marker>')
    svg.append('  </defs>')

    # ROW 1: Top pipeline flow (fits within 900px)

    # Step 1: Audio Recording
    svg.append('  <rect x="40" y="40" width="160" height="140" fill="#fff" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="120" y="70" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Audio</text>')
    svg.append('  <text x="120" y="96" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Recording</text>')
    # Waveform visualization
    svg.append('  <path d="M 50 135 Q 65 115 80 135 T 110 135 T 140 135 T 170 135 T 190 135" fill="none" stroke="#8B1A1A" stroke-width="2.5"/>')
    svg.append('  <path d="M 50 145 Q 65 155 80 145 T 110 145 T 140 145 T 170 145 T 190 145" fill="none" stroke="#8B1A1A" stroke-width="2.5"/>')

    # Arrow 1
    svg.append('  <path d="M 200 110 L 240 110" stroke="#000" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>')

    # Step 2: Mel Spectrogram
    svg.append('  <rect x="240" y="40" width="160" height="140" fill="#fff" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="320" y="70" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Mel</text>')
    svg.append('  <text x="320" y="96" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Spectrogram</text>')
    # Spectrogram visualization (gradient bars)
    for i in range(8):
        y = 120 + i * 7
        opacity = 0.3 + (i * 0.08)
        svg.append(f'  <rect x="260" y="{y}" width="120" height="6" fill="#8B1A1A" opacity="{opacity}"/>')

    # Arrow 2
    svg.append('  <path d="M 400 110 L 440 110" stroke="#000" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>')

    # Step 3: AMT
    svg.append('  <rect x="440" y="40" width="160" height="140" fill="#fff" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="520" y="70" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">AMT</text>')
    svg.append('  <text x="520" y="110" font-family="Roboto Mono, monospace" font-size="15" text-anchor="middle" fill="#666">Neural network</text>')
    svg.append('  <text x="520" y="130" font-family="Roboto Mono, monospace" font-size="15" text-anchor="middle" fill="#666">transcription</text>')
    # Neural network icon
    for i, x in enumerate([470, 520, 570]):
        svg.append(f'  <circle cx="{x}" cy="160" r="6" fill="#8B1A1A"/>')

    # Arrow 3
    svg.append('  <path d="M 600 110 L 640 110" stroke="#000" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>')

    # Step 4: Student MIDI
    svg.append('  <rect x="640" y="40" width="160" height="140" fill="#fff" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="720" y="70" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Student</text>')
    svg.append('  <text x="720" y="96" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">MIDI</text>')
    # Piano roll visualization
    svg.append('  <rect x="660" y="120" width="18" height="45" fill="#000" opacity="0.7"/>')
    svg.append('  <rect x="688" y="130" width="15" height="35" fill="#000" opacity="0.7"/>')
    svg.append('  <rect x="705" y="115" width="18" height="50" fill="#000" opacity="0.7"/>')
    svg.append('  <rect x="730" y="125" width="22" height="40" fill="#000" opacity="0.7"/>')
    svg.append('  <rect x="760" y="135" width="16" height="30" fill="#000" opacity="0.7"/>')

    # Arrow from Student MIDI down toward Alignment
    svg.append('  <path d="M 720 180 L 720 220 L 320 220 L 320 260" stroke="#000" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>')

    # ROW 2: Reference MIDI, Alignment, Error Detection, Output

    # Reference MIDI (bottom left)
    svg.append('  <rect x="40" y="260" width="160" height="140" fill="#fff" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="120" y="295" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Reference</text>')
    svg.append('  <text x="120" y="321" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">MIDI</text>')
    # Piano roll visualization
    svg.append('  <rect x="60" y="350" width="18" height="40" fill="#000" opacity="0.5"/>')
    svg.append('  <rect x="85" y="355" width="18" height="35" fill="#000" opacity="0.5"/>')
    svg.append('  <rect x="108" y="348" width="20" height="42" fill="#000" opacity="0.5"/>')
    svg.append('  <rect x="133" y="353" width="22" height="37" fill="#000" opacity="0.5"/>')
    svg.append('  <rect x="160" y="358" width="18" height="32" fill="#000" opacity="0.5"/>')

    # Arrow from Reference to Alignment
    svg.append('  <path d="M 200 330 L 240 330" stroke="#000" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>')

    # Alignment (bottom middle)
    svg.append('  <rect x="240" y="260" width="160" height="140" fill="#fff" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="320" y="295" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Alignment</text>')
    svg.append('  <text x="320" y="330" font-family="Roboto Mono, monospace" font-size="15" text-anchor="middle" fill="#666">Match student</text>')
    svg.append('  <text x="320" y="350" font-family="Roboto Mono, monospace" font-size="15" text-anchor="middle" fill="#666">to reference</text>')
    # Connection lines visualization
    svg.append('  <line x1="260" y1="370" x2="300" y2="375" stroke="#666" stroke-width="1.5"/>')
    svg.append('  <line x1="270" y1="380" x2="310" y2="378" stroke="#666" stroke-width="1.5"/>')
    svg.append('  <line x1="280" y1="385" x2="320" y2="382" stroke="#666" stroke-width="1.5"/>')
    svg.append('  <line x1="350" y1="370" x2="390" y2="375" stroke="#666" stroke-width="1.5"/>')
    svg.append('  <line x1="360" y1="380" x2="400" y2="378" stroke="#666" stroke-width="1.5"/>')

    # Arrow from Alignment to Error Detection
    svg.append('  <path d="M 400 330 L 440 330" stroke="#000" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>')

    # Error Detection
    svg.append('  <rect x="440" y="260" width="160" height="140" fill="#fff" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="520" y="295" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Error</text>')
    svg.append('  <text x="520" y="321" font-family="Roboto Mono, monospace" font-size="20" text-anchor="middle" fill="#000" font-weight="bold">Detection</text>')
    svg.append('  <text x="520" y="355" font-family="Roboto Mono, monospace" font-size="15" text-anchor="middle" fill="#E74C3C">Incorrect notes</text>')
    svg.append('  <text x="520" y="375" font-family="Roboto Mono, monospace" font-size="15" text-anchor="middle" fill="#3498DB">Missing notes</text>')
    svg.append('  <text x="520" y="395" font-family="Roboto Mono, monospace" font-size="15" text-anchor="middle" fill="#F39C12">Extra notes</text>')

    # Arrow to output
    svg.append('  <path d="M 600 330 L 640 330" stroke="#000" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>')

    # Final output
    svg.append('  <rect x="640" y="260" width="160" height="140" fill="#f8f8f8" stroke="#666" stroke-width="2" rx="5"/>')
    svg.append('  <text x="720" y="295" font-family="Roboto Mono, monospace" font-size="18" text-anchor="middle" fill="#000" font-weight="bold">Annotated</text>')
    svg.append('  <text x="720" y="321" font-family="Roboto Mono, monospace" font-size="18" text-anchor="middle" fill="#000" font-weight="bold">Score</text>')
    # Staff lines
    for i in range(5):
        y = 360 + i * 8
        svg.append(f'  <line x1="655" y1="{y}" x2="785" y2="{y}" stroke="#bbb" stroke-width="1.5"/>')
    # Note icons (good, good, incorrect, missing, good)
    good_color = '#000000'
    incorrect_color = '#E74C3C'
    missing_color = '#3498DB'
    notes = [
        (670, 382, good_color, 'solid'),        # good
        (700, 370, good_color, 'solid'),        # good
        (730, 376, incorrect_color, 'solid'),   # incorrect
        (755, 364, missing_color, 'missing'),   # missing
        (780, 380, good_color, 'solid')         # good
    ]
    for x, cy, color, style in notes:
        if style == 'missing':
            svg.append(f'  <ellipse cx="{x}" cy="{cy}" rx="8" ry="5" fill="{color}" stroke="{color}" stroke-width="2"/>')
            svg.append(f'  <rect x="{x + 6}" y="{cy - 35}" width="3" height="35" fill="{color}"/>')
        else:
            svg.append(f'  <ellipse cx="{x}" cy="{cy}" rx="8" ry="5" fill="{color}" stroke="{color}" stroke-width="1.5"/>')
            svg.append(f'  <rect x="{x + 6}" y="{cy - 32}" width="3" height="32" fill="{color}"/>')

    svg.append('</svg>')

    with open(output_path, 'w') as f:
        f.write('\n'.join(svg))

    print(f"Generated {output_path}")

if __name__ == '__main__':
    generate_pipeline_svg('images/music-ai-pipeline.svg')
