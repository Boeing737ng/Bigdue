#figure 4 

install.packages ("dplyr")
install.packages ("ggplot2")
install.packages ("reshape2")
install.packages ("grid")
library(dplyr)  
library(ggplot2)
library(reshape2)
library(grid)


# packet 
# packet_local <- read.csv(file="C:/Users/Jaesung/Desktop/Bigdue/Bigdue/static/data/merge.csv", sep=",")
packet_local <- read.csv(file="C:/Users/Hanul-Park/Desktop/Bigdue/Bigdue/static/data/merge_count.csv", sep=",")
str(packet_local)

# Varibles
Xintercept<-3000
Title_CF="CDF of Distance vs Packet Size [n Packets]\n"
RTTs = packet_local$rtt
Distance = packet_local$distance
# Size = packet_local$size
Count = packet_local$count

packet_local <- packet_local[order(Distance),]

# CF_local <- mutate(packet_local, cum_frequency=cumsum(Size))
CF_local <- mutate(packet_local, cum_frequency=cumsum(Count))
# CF_local <- mutate(CF_local,  percentage=CF_local$cum_frequency / sum(Size))
CF_local <- mutate(CF_local,  percentage=CF_local$cum_frequency / sum(Count))
CF_local <- rbind(c(0,0,0,0,0,0,0,0,0), CF_local)
CF_local # check percentage sum up to 1.0

# Size_of_Packets = utils:::format.object_size(sum(Size), "auto")
Count_of_Packets = utils:::format.object_size(sum(Count), "auto")
Title_CF=paste("CDF of Distance vs Packet Size [", Count_of_Packets, "of Packets]\n")


legend_detail <- c("Foreign User"="#f04546", "Local User"="#3591d1") #red
f2 <- approxfun(CF_local$distance, CF_local$percentage)

Yintercept<-f2(Xintercept)

graph_CF<-ggplot() +
  geom_step(data=CF_local, aes(x=distance, y=percentage))  +
  
  labs(x="Distance(km)", y="CDF")+
  scale_color_manual(name="Index\n", values=legend_detail)+
  theme(axis.text=element_text(size=14), axis.title.y = element_text(size = rel(1.5), angle = 90), 
        axis.title.x = element_text(size = rel(1.5), angle = 00))+
  #geom_vline(xintercept = Xintercept, linetype="dotted", color = "black", size=1.0)+
  #geom_hline(yintercept = Yintercept, linetype="dotted", color = "black", size=1.0)+
  geom_segment(mapping=aes(x=3000, xend=3000, y=0, yend=Yintercept), linetype="dotted", size=1.0)+
  geom_segment(mapping=aes(x=0, xend=3000, y=Yintercept, yend=Yintercept), linetype="dotted", size=1.0)+
  scale_x_continuous(expand = c(0.01,0))+
  scale_y_continuous(expand = c(0,0.02))+
  geom_text(mapping=aes(x=0, y=Yintercept), label=round(Yintercept, 3), hjust=1.4, col="black", size=4)+
  geom_text(mapping=aes(x=Xintercept, y=0), label=Xintercept, vjust=2.3, col="black", size=4)

graph_CF_without_clipping <- ggplot_gtable(ggplot_build(graph_CF))
graph_CF_without_clipping$layout$clip[graph_CF_without_clipping$layout$name == "panel"] <- "off"
grid.draw(graph_CF_without_clipping)


