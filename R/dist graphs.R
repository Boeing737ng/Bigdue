#install.packages ("dplyr")
install.packages ("ggplot2")
install.packages ("reshape2")
library(dplyr)  
library(ggplot2)
library(reshape2)

# CDF RTT vs Size

########## First packet table ###############
packet <- read.csv(file="C:/Users/Jaesung/Desktop/merge.csv", sep=",")
Size_of_Packets = utils:::format.object_size(sum(Size), "auto")

# Distribution diagram : RTT vs Distance & RTT vs Size
plot(cumulative_frequencies$rtt, cumulative_frequencies$distance,
     xlim = c(0,0.3),
     ylim = c(0,16000),
     xlab="RTT",
     ylab="Distance",
     main=paste("Relationship between RTT & Distance [",Size_of_Packets,"of packets]"))
RTTs<-cumulative_frequencies$rtt
Dis<-cumulative_frequencies$distance
cor(Dis, RTTs, method=c("pearson"))

plot(cumulative_frequencies$size, cumulative_frequencies$distance,
     xlim = c(0,2500),
     ylim = c(0,16000),
     xlab="Size",
     ylab="Distance",
     main=paste("Relationship between Size & Distance [",Size_of_Packets,"of packets]"))
