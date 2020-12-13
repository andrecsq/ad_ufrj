# ReedFrost.R
# Exercise 1.25
# Simulate graphs in Figure 1.2

par(mfrow=c(2,2))
set.seed(17)

for (k in 1:16) {
  z = 0.004
  steps  <- 25
  sus <- numeric(steps)
  inf <- numeric(steps)
  
  # When sus = 400, max is 30 infected
  sus[1] <- 300
  # When inf[1] = 3, max(inf) = 
  inf[1] <- 5
  
  for (t in 1:(steps-1)) {
    inf[t+1] <- rbinom(1,sus[t],1-(1-z)^inf[t])
    sus[t+1] <- sus[t] - inf[t+1]
  }
  
  print(paste0("Iteration #", k))
  print(paste0("Max value: ", max(inf)))
  print(paste0("Mean value: ", mean(inf)))
  print(paste0("Total infected: ", sum(inf)))
  print(paste0("% infected: ", round((sum(inf)/sus[1])*100, 2), "%"))
  print(paste0("Day of erradication: ", match(0, inf)))
    
  print("----------------------")
  plot((0:(steps-1)),inf,type="o",yaxt="n",xlab="Time",ylab="Infected")
  axis(2)
}
#seed: 12