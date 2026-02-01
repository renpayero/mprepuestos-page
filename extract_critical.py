import re

with open('styles.css', 'r') as f:
    css = f.read()

# Find the start of brands section to cut before it
split_marker = "/* Brands Section Modern Marquee */"
critical_css = css.split(split_marker)[0]

# Minify
# Remove comments
critical_css = re.sub(r'/\*.*?\*/', '', critical_css, flags=re.DOTALL)
# Remove whitespace
critical_css = re.sub(r'\s+', ' ', critical_css)
critical_css = re.sub(r'\s*([:;{}])\s*', r'\1', critical_css)
critical_css = critical_css.replace(';}', '}')

with open('critical.min.css', 'w') as f:
    f.write(critical_css)

print(f"Extracted critical CSS: {len(critical_css)} bytes")
