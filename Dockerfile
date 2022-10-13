FROM python:3.8.12
RUN apt-get -y update
RUN apt-get -y install make automake g++ \
               libpoppler-glib-dev poppler-utils \
               libwxgtk3.0-gtk3-dev xvfb

RUN git clone https://github.com/vslavik/diff-pdf.git
WORKDIR diff-pdf
RUN ./bootstrap
RUN ./configure
RUN make 
RUN make install