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



# plot
install.packages ("dplyr")
install.packages ("ggplot2")
install.packages ("reshape2")
library(dplyr)  
library(ggplot2)
library(reshape2)




init <- function() {
  setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
  t <- list.files()
  
  df <- data.frame()
  
  for (name in t) {
    setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
    print(paste0(getwd(),"/",name,"/","distance"))
    setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
    setwd(toString(paste0(getwd(),"/",name,"/","distance")))
    
    packet <- list.files(pattern = "*.csv")
    packet <- strsplit(packet, " ")
    packet <- toString(packet[2])
    packet <- read.csv(file = packet)
    
    packet <- packet[(packet$rtt >= 0.1),]
    # packet <- packet[(packet$distance >= 0)&(packet$distance <= 6720.495),]
    # packet <- packet[(packet$rtt <= 0.4)&(packet$rtt >= 0.1),]    
    # packet <- packet[(packet$size <= 1000000)&(packet$size > 0),]
    
    df <- rbind(df, packet)
  }
  return(df)
}




# 1
df <- init()
# write.csv(df, "C:/Users/Hanul-Park/Documents/카카오톡 받은 파일/merge.csv")
# str(df)
summary(df)
# par( mfrow =c(1, 2))
correlation <- cor(df$rtt,df$distance)
plot(x = df$rtt, y = df$distance, xlab ="RTT",
     ylab ="Distance", main =paste("RTT x Distance", "/", round(correlation, digits = 2)))

# lm(종속변수~독립변수)
res = lm(df$distance~df$rtt)
abline(res, col = "red", lwd = 1)




# 2
df <- init()

str(df)
summary(df)
# par( mfrow =c(1, 2))
# plot(x = df$rtt, y = df$distance, xlab ="RTT",
#      ylab ="Distance", main ="RTT x Distance")

correlation <- cor(df$rtt,df$size)
plot(x = df$rtt, y = df$size, xlab ="RTT",
     ylab ="Size", main =paste("RTT x Size", "/", round(correlation, digits = 2)))

res = lm(df$size~df$rtt)
abline(res, col = "red", lwd = 1)

a <- c(1, 2, 3, 4, 5, 6, 7)
b <- c(7, 6, 5 ,4, 3, 2, 1)
c <- c(2, 2, 2, 2, 3, 2, 2)
cor(a,c)
plot(a,c)
res = lm(c~a)
abline(res, col = "red", lwd = 1)



# 3
df <- init()
# str(packet)
# df <- df[order(df$rtt),]
df <- df[order(df$distance),]
df

outlier<-df
cumulative_frequencies <- mutate(outlier, cum_frequency=cumsum(outlier$size))
cumulative_frequencies  
cumulative_frequencies <- mutate(cumulative_frequencies, 
                                 percentage
                                 =cumulative_frequencies$cum_frequency / 
                                   sum(cumulative_frequencies$size))

cumulative_frequencies <- rbind(c(0,0,0,0,0,0,0,0,0), cumulative_frequencies)
cumulative_frequencies


# plot(x = cumulative_frequencies$rtt, y = cumulative_frequencies$percentage, xlab ="RTT(ms)",
#      ylab ="Packet Size(%)", main ="CDF of RTT vs Packet Size [1 Millon Packets]\n", type = "l")

plot(x = cumulative_frequencies$distance, y = cumulative_frequencies$percentage, xlab ="Distance(km)",
     ylab ="Packet Size(%)", main ="CDF of RTT vs Packet Size [1 Millon Packets]\n", type = "l")

res = lm(cumulative_frequencies$percentage~cumulative_frequencies$distance)
abline(res, col = "red", lwd = 1)




# 4
i <- 65
alphabet  <- function(x) { rawToChar(as.raw(x)) }

setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
file_list <- list.files()

# name_list <- c()
# df <- data.frame()
# par(new = T)
par( mfrow =c(3, 5))
# par( mfrow =c(1, 1))

for (name in file_list) {
  setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
  print(paste0(getwd(),"/",name,"/","distance"))
  setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
  setwd(toString(paste0(getwd(),"/",name,"/","distance")))
  
  packet <- list.files(pattern = "*.csv")
  packet <- strsplit(packet, " ")
  packet <- toString(packet[2])
  packet <- read.csv(file = packet)
  
  ifelse(packet$rtt > 9000,print(name),print(""))
  packet <- packet[(packet$rtt <= 0.4)&(packet$rtt > 0) ,]
  packet <- packet[order(packet$distance),]
  
  # df <- packet
  # name_list <- c(name_list, name)
  
  # packet <- cbind(packet, name)
  # df <- rbind(df, packet)
  
  # par(new = T)
  # plot(x = df$distance, y = df$rtt, col = df$name, type = "l")
  
  # plot(x = packet$rtt, y = packet$distance, xlab ="RTT",
  #      ylab ="Distance", type = "p", main = alphabet(i))
  # i <- i+1

  correlation <- cor(packet$rtt,packet$distance)
  
  plot(x = packet$rtt, y = packet$distance, xlab ="RTT",
       ylab ="Distance", type = "p", main = paste(alphabet(i), "/", round(correlation, digits = 2)))
  i <- i+1
  # plot(x = packet$rtt, y = packet$size, xlab ="RTT",
  #      ylab ="Size", type = "p", main = name)
  
  res = lm(packet$distance~packet$rtt)
  # res = lm(packet$size~packet$rtt)
  abline(res, col = "red", lwd = 1)
}



# 5
install.packages("moonBook")
library(moonBook)


setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
t <- list.files()

df <- data.frame()

for (name in t) {
  setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
  print(paste0(getwd(),"/",name,"/","distance"))
  setwd("C:/Users/Hanul-Park/Desktop/테스트결과")
  setwd(toString(paste0(getwd(),"/",name,"/","distance")))
  
  packet <- list.files(pattern = "*.csv")
  packet <- strsplit(packet, " ")
  packet <- toString(packet[2])
  packet <- read.csv(file = packet)
  
  packet <- packet[(packet$rtt <= 0.4)&(packet$rtt > 0) ,]
  packet <- cbind(packet, name)
  
  df <- rbind(df, packet)
}

df

data(df)
str(df)

mytable(name~rtt,data=df)
