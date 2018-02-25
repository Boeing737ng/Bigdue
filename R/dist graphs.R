#install.packages ("dplyr")
install.packages ("ggplot2")
install.packages ("reshape2")
library(dplyr)  
library(ggplot2)
library(reshape2)

# CDF RTT vs Size

########## First packet table ###############
# packet <- read.csv(file="C:/Users/Jaesung/Desktop/Bigdue/Bigdue/static/data/merge.csv", sep=",")
packet <- read.csv(file="C:/Users/Hanul-Park/Desktop/Bigdue/Bigdue/static/data/merge.csv", sep=",")
Size_of_Packets = utils:::format.object_size(sum(packet$size), "auto")

Corr_table <- subset(packet, 0<packet$rtt & packet$rtt<0.1)
RTTs<-Corr_table$rtt
Dis<-Corr_table$distance
cor(Dis, RTTs, method=c("pearson"))

RTTs<-packet$rtt
Dis<-packet$distance

# Distribution diagram : RTT vs Distance & RTT vs Size
plot(Dis, RTTs,
     xlim = c(0,16000),
     ylim = c(0,1),
     xlab="Distance",
     ylab="RTT",
     main=paste("Relationship between RTT & Distance [",Size_of_Packets,"of packets]"))
cor(packet$distance, packet$rtt, method=c("pearson"))

plot(packet$size, packet$distance,
    xlim = c(0,2500),
     ylim = c(0,16000),
     xlab="Size",
     ylab="Distance",
     main=paste("Relationship between Size & Distance [",Size_of_Packets,"of packets]"))

plot(packet$size, packet$rtt, 
     xlim = c(0,2000),
     ylim = c(0,0.3),
     xlab="Size",
     ylab="RTT",
     main=paste("Relationship between RTT & Size [",Size_of_Packets,"of packets]"))

