FROM hugome/gcc-multilib
WORKDIR /usr/src
COPY 10KIA748.s /usr/src
RUN gcc -m32 10KIA748.s -o 10KIA748 -g
CMD ["./10KIA748"]
