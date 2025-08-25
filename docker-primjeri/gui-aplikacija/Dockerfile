FROM python:3.13-slim

# Install system dependencies for PyQt6 and X11
RUN apt-get update && apt-get install -y \
    git \
    libgl1 \
    libegl1 \
    libqt6core6 \
    libqt6gui6 \
    libqt6widgets6 \
    libx11-xcb1 \
    libxcb1 \
    libxcb-glx0 \
    libxcb-keysyms1 \
    libxcb-image0 \
    libxcb-shm0 \
    libxcb-icccm4 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-shape0 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-cursor0 \
    libxrender1 \
    libsm6 \
    libice6 \
    libxext6 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libxrandr2 \
    libxinerama1 \
    libfontconfig1 \
    fonts-dejavu-core \
    xauth \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/limafresh/pyqulator.git

# Install Python dependencies
RUN pip install --no-cache-dir PyQt6
RUN pip install --no-cache-dir sympy==1.14.0

# Set Qt to use X11
ENV QT_QPA_PLATFORM=xcb

WORKDIR /pyqulator/pyqulator

# Default command
CMD ["python", "main.py"]
