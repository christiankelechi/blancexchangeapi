import base64

# The base64 string provided
qr_code_base64 = "iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAACgUlEQVR4nO2aQW7bMBBF31QCvKSAHiBHoW/WM+UG0lFygALi0gCF3wVJyUlaJEEcxSpGC1mW3+ID38OZIcfER67px4dwcN5555133nnn/8VbvXrsnPrylcnM7Jzab+cd9Th/K74vH3EESD/RNGAQZiwKIHUZANtHj/Nfw6caoXamkzQDpJ7yzqzfW4/zt+H7v720+DggyPvrcf6L+aiLAZ3MhsU0frce5z/Ft/gNAhKINKDp4WLEccHiI1xvgdybfuffxU9mZjbU/Gu/nk6CdBKwlPJ5Xz3O34gv8btFqEgA4WJMQ4eeR+/96Xf+PXyN0FIwL8Y0AHGuT7Ux3lGP87fi1/z7u4eQEanLRuoR5N7ik7XueBc9zt+WR5IEdCLOUAvmIGmkk6QMlCdJ473pd/6Nq/oWMhCq05Iy5TYWJEN0fw/IV381110rjSWSO2kMak7PHr8H5ev6HGdKhBKVIc6d6q/NWo/fQ/ItfovJaxCHumaXdLy67/4ejWezFkIuXhaTNXe1yBqDx+9BebbFt5m8LtczlJ7J8+9h+VY/r1Xz2M4Ht8Ts+fe4/HX80tbimnXVnrz/PSy/9ketzWWtqq5cdX8Pzk8DQOpr/wu1P2qjV4vPXx2Tv+qPrtLsVlPHZ+88fo/Gr/vPQFmQ53prlfS60+H+HpePLQlDuJSTfumpp/bE21/gTvU7/waf1glnQNLF7BxyGexgGhaf3/g/eLOBVm6xWD1TSifZ+Vv0OH9rPp3K/JXGUk4vVk8Pv0mP85/hX85PllmN6SFjcczrdPTSax89zt+Wf1k/E9ej/VpuZbbtSq+fj8a/np/c9jeC2quwAvem33nnnXfeeeePyP8BDJsInqZ/TSUAAAAASUVORK5CYII="

# Decode the base64 string
qr_code_data = base64.b64decode(qr_code_base64)

# Save the decoded bytes as an image file
with open("qr_code.png", "wb") as f:
    f.write(qr_code_data)

print("QR code saved as 'qr_code.png'")
