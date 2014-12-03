//stores one diskstat sample; used in "report" class
class reportlet{

long sectors_read;
long sectors_written;
//fields 1 (reads, where 1 read = 1 sector), 5 (writes, where 1 write = 1 sector), 
// and calculate from that based on deltas in time (for /s)
// or(and) 1 sector or block being 1 KB

}