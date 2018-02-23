getwd()

# 경로 설정 - csv file 있는 곳으로
setwd("C:/Users/Hanul-Park/Desktop/Bigdue/Bigdue/static/data/distance")
csv_data<-read.csv("1519073224880_edge_distance_count.csv",header=T)

# head(csv_data)
#summary(csv_data)
# str(csv_data)
#remove(txt_data)

# x <- csv_data[c(6,7)]
# x
# cor(x)

# rtt 조건범위 설정. ex) rtt 200ms 이상.
csv_data$criteria <- ifelse(csv_data$rtt>=0.2,1,0)
# csv_data
# 조건에 맞는 데이터만 추출.
test_data <- csv_data[csv_data$criteria == 1,]
# test_data

# distance, rtt data만 추출
x <- test_data[6]
y <- test_data[7]

# correlation coefficient 구하기. 
correlation <- cor(x,y)
correlation 

# test_data <- test_data[c(6,7)]
# test_data
# cor(test_data)

# csv file 저장.
write.csv(correlation, "C:/Users/Hanul-Park/Desktop/Bigdue/Bigdue/static/data/correlation_coefficient.csv")


install.packages ("dplyr")
install.packages ("ggplot2")
install.packages ("reshape2")
library(dplyr)  
library(ggplot2)
library(reshape2)


# setwd("C:/Users/Hanul-Park/Desktop/테스트결과/고석규/distance")
setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
t <- list.files()
t

l <- c()
l2 <- c()
par(new=T)


for (name in t) {
  setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
  print(paste0(getwd(),"/",name,"/","distance"))
  setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
  setwd(toString(paste0(getwd(),"/",name,"/","distance")))
  
  packet <- list.files(pattern = "*.csv")
  packet <- strsplit(packet, " ")
  packet <- toString(packet[2])
  packet <- read.csv(file = packet)
  
  str(packet)
  packet <- packet[order(packet$rtt),]
  
  outlier<-packet
  cumulative_frequencies <- mutate(outlier, cum_frequency=cumsum(outlier$size))
  cumulative_frequencies  
  
  cumulative_frequencies <- mutate(cumulative_frequencies, 
                                   percentage
                                   =cumulative_frequencies$cum_frequency / 
                                     sum(cumulative_frequencies$size))
  
  cumulative_frequencies <- rbind(c(0,0,0,0,0,0,0,0,0), cumulative_frequencies)
  cumulative_frequencies
  
  l <- c(l, name)
  l2 <- c(l2, cumulative_frequencies)
  plot(x = cumulative_frequencies$rtt, y = cumulative_frequencies$percetage, type = "l")
  # lines(x = cumulative_frequencies$rtt, y = cumulative_frequencies$percetage)
}


legend_detail <- c("Foreign User"="#f04546", "Local User"="#3591d1") #red
ggplot() +
  #  geom_step(data=cumulative_frequencies2, aes(x=rtt, y=percentage, color="Local User"))  +
  
  geom_step(data=cumulative_frequencies, aes(x=rtt, y=percentage, color="Foreign User"))  +
  
  labs(x="RTT(ms)", y="Packet Size(%)", title="CDF of RTT vs Packet Size [1 Millon Packets]\n")+
  scale_color_manual(name="Index\n", values=legend_detail)+
  theme(plot.title = element_text(hjust = 0.5))+xlim(0,0.34)


plot(cumulative_frequencies$rtt, cumulative_frequencies$distance,
     xlim = c(0,0.3),
     ylim = c(0,16000),
     xlab="RTT",
     ylab="Distance",
     main="Relationship between RTT & Distance (Foreigner Group)")
RTTs<-cumulative_frequencies$rtt
Dis<-cumulative_frequencies$distance
cor(Dis, RTTs, method=c("pearson"))

plot(cumulative_frequencies$size, cumulative_frequencies$distance,
     xlim = c(0,2000000),
     ylim = c(0,16000),
     xlab="Size",
     ylab="Distance",
     main="Relationship between Size & Distance")


cdf_fun <- ecdf(packet$distance)  
plot(cdf_fun, xlab="RTT",  ylab="Fraction of Data",main="CDF")