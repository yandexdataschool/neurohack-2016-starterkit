f <- file("stdin")
open(f)
OFFSET <- 3000
experiment_id <- readLines(f, n=1, warn=FALSE)
alpha <- 0.1
data_avg <- 0

for (i in 1:OFFSET) {
    line <- readLines(f, n=1, warn=FALSE)
    cur_data <- as.numeric(unlist(strsplit(line, split=" ", fixed=TRUE)))
    data_avg <- alpha * data_avg + (1 - alpha) * cur_data[[16]]
}

write(data_avg, stdout())
flush.console()

while (1) {
    line <- readLines(f, n=1, warn=FALSE)
    cur_data <- as.numeric(unlist(strsplit(line, split=" ", fixed=TRUE)))
    data_avg <- alpha * data_avg + (1 - alpha) * cur_data[[16]]
    write(data_avg, stdout())
    flush.console()
}
