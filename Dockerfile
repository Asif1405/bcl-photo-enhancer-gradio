FROM nvidia/cuda:11.6.1-cudnn8-devel-ubuntu20.04

# set non interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update --yes --quiet && \
    apt-get install -y ffmpeg unzip gcc cmake wget && \
    apt-get install -y python3.8 python3-pip python3.8-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY req.txt /app/req.txt

# Install the requirements
RUN pip install --upgrade pip
RUN pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install -r req.txt
RUN pip install gdown

# Copy the content of the local src directory to the working directory
COPY . /app

# IF PE_4_3_24 folder is not present, download it
RUN if [ ! -d "PE_4_3_24" ]; then gdown https://drive.google.com/uc?id=1-3Z -O PE_4_3_24.zip; unzip PE_4_3_24.zip; rm PE_4_3_24.zip; fi

# Download the model
RUN wget "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth" -O GFPGANv1.4.pth
# move the model to /usr/local/lib/python3.8/dist-packages/gfpgan/weights/
RUN mv GFPGANv1.4.pth /usr/local/lib/python3.8/dist-packages/gfpgan/weights/GFPGANv1.4.pth

# Expose the port
EXPOSE 3005

# Run the command
CMD ["python3.8", "main.py"]
