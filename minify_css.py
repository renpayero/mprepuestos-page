import re

with open('styles.css', 'r') as f:
    css = f.read()

# Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
# Remove whitespace
css = re.sub(r'\s+', ' ', css)
css = re.sub(r'\s*([:;{}])\s*', r'\1', css)
css = css.replace(';}', '}')

with open('styles.min.css', 'w') as f:
    f.write(css)

print("Minified styles.css to styles.min.css")
