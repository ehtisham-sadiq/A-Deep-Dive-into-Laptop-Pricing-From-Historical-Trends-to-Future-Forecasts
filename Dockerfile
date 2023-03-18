# Use an official Python runtime as a parent image
FROM python:3.7

CMD mkdir /app


# Copy the current directory contents into the container at /app
COPY . /app


# Set the working directory to /app
WORKDIR  /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Expose the port for Streamlit
EXPOSE 8501

# Run app.py when the container launches
CMD streamlit run app.py