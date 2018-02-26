#install.packages ("dplyr")
install.packages ("ggplot2")
install.packages ("reshape2")
library(dplyr)  
library(ggplot2)
library(reshape2)

# CDF RTT vs Size

########## First packet table ###############
# packet <- read.csv(file="C:/Users/Jaesung/Desktop/Bigdue/Bigdue/static/data/merge.csv", sep=",")
packet <- read.csv(file="C:/Users/Hanul-Park/Desktop/Bigdue/Bigdue/static/data/merge_size.csv", sep=",")
Size_of_Packets = utils:::format.object_size(sum(packet$size), "auto")

Corr_table <- subset(packet, 0<packet$rtt & packet$rtt<0.1)

RTTs<-Corr_table$rtt
Dis<-Corr_table$distance
cor(Dis, RTTs, method=c("pearson"))

packet<-packet[(packet$rtt>=0)&(packet$rtt<0.4),]
packet<-packet[(packet$distance>=0)&(packet$distance<15000),]

RTTs<-packet$rtt
Dis<-packet$distance

# Distribution diagram : RTT vs Distance & RTT vs Size
plot(Dis, RTTs*1000,
     xlim = c(0,15000),
     ylim = c(0,400),
     xlab="Distance(Km)",
     ylab="RTT(ms)", cex.lab = 1.5, axes = F)
axis(side=1, labels=T, cex.axis = 1.5)
axis(side=2, labels=T, cex.axis = 1.5)
# main=paste("Relationship between RTT & Distance [",Size_of_Packets,"of packets]")
# Dis <- Dis[(Dis>=0)&(Dis<=16000)]
# RTTS <- RTTs[(RTTs>=0)&(RTTs<=1)]
# res <- lm((RTTs*1000)~Dis)
# abline(res, col = "red", lwd = 2)
# cor((RTTs*1000),Dis)

packet <- read.csv(file="C:/Users/Hanul-Park/Desktop/Bigdue/Bigdue/static/data/merge_size.csv", sep=",")
packet<-packet[(packet$distance>=0)&(packet$distance<15000),]
packet<-packet[(packet$size>=0)&(packet$size<2500),]

plot(packet$size, packet$distance,
    xlim = c(0,2500),
     ylim = c(0,15000),
     xlab="Data Size(Bytes)",
     ylab="Distance(Km)", cex.lab = 1.5, axes = F)
axis(side=1, labels=T, cex.axis = 1.5)
axis(side=2, labels=T, cex.axis = 1.5)
# main=paste("Relationship between Size & Distance [",Size_of_Packets,"of packets]")
# res <- lm(packet$distance~packet$size)
# abline(res, col = "red", lwd = 2)
# cor(packet$distance,packet$size)




packet <- read.csv(file="C:/Users/Hanul-Park/Desktop/Bigdue/Bigdue/static/data/merge_size.csv", sep=",")
packet<-packet[(packet$rtt>=0)&(packet$rtt<0.4),]
packet<-packet[(packet$size>=0)&(packet$size<2500),]

plot(packet$size, packet$rtt*1000, 
     xlim = c(0,2500),
     ylim = c(0,400),
     xlab="Data Size(Bytes)",
     ylab="RTT(ms)", cex.lab = 1.5, axes = F)
axis(side=1, labels=T, cex.axis = 1.5)
axis(side=2, labels=T, cex.axis = 1.5, at = c(0, 100, 200, 300, 400))
# main=paste("Relationship between RTT & Size [",Size_of_Packets,"of packets]")
# res <- lm((packet$rtt*1000)~packet$size)
# abline(res, col = "red", lwd = 2)
# cor((packet$rtt*1000),packet$size)

