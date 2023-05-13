def all_bits_on():
    
    for i in all_bits_set:
        for j in range(16):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])

def top_rows():
    
    top_rows=[
        top_1rows,top_2rows,
        top_3rows,top_4rows]
    
    for x in range(4):
        for i in top_rows[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def bottom_rows():
    
    bottom_rows=[
        bottom_1rows,bottom_2rows,
        bottom_3rows,bottom_4rows]
    
    for x in range(4):
        for i in bottom_rows[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def top_bottom_rows_open():
    
    top_bottom_rows_open=[
        top_bottom_1rows,top_bottom_2rows,
        top_bottom_3rows,top_bottom_4rows]
    
    for x in range(3,-1,-1):
        for i in top_bottom_rows_open[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def top_bottom_rows_close():
    
    top_bottom_rows_close=[
        top_bottom_1rows,top_bottom_2rows,
        top_bottom_3rows,top_bottom_4rows]
    
    for x in range(4):
        for i in top_bottom_rows_close[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def right_columns():
    
    right_columns=[
        right_1columns,right_2columns,
        right_3columns,right_4columns]
    
    for x in range(4):
        for i in right_columns[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def left_columns():
    
    left_columns=[
        left_1columns,left_2columns,
        left_3columns,left_4columns]
    
    for x in range(4):
        for i in left_columns[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def right_left_columns_open():
    
    right_left_columns_open=[
        right_left_1columns,
        right_left_2columns,
        right_left_3columns,
        right_left_4columns]
    
    for x in range(3,-1,-1):
        for i in right_left_columns_open[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def right_left_columns_close():
    
    right_left_columns_close=[
        right_left_1columns,
        right_left_2columns,
        right_left_3columns,
        right_left_4columns]
    
    for x in range(4):
        for i in right_left_columns_close[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def cascade_up_down():
    
    cascade_up_down=[
        cascade_up,cascade_down]
    
    for y in range(4):
        for x in range(2):
            for i in cascade_up_down[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def cascade_right_left():
    
    cascade_right_left=[
        cascade_right,cascade_left]
    
    for y in range(4):
        for x in range(2):
            for i in cascade_right_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
            
def random_bits():
    
    for i in range(16):
        randbit=random.randint(0,1)
        GPIO.output(latch,0)
        GPIO.output(data_bit,randbit)
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed[1])