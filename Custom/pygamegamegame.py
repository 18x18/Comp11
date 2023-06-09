if square.y + square.height < HEIGHT: 
                square.y += GRAV 
            if not square.colliderect(i) or  square.y + square.height != HEIGHT:
                air_time -= 1   
            if square.colliderect(i) or square.y + square.height == HEIGHT:
                air_time = 10