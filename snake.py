import pygame  # import the libraries 

pygame.init()  

gameExit = False
print("Hello Friends!!!!")

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

display_height = 600
display_width  = 600

gameDisplay = pygame.display.set_mode((display_height,display_width))# creating a simple window 
pygame.display.set_caption('ratnsnake')  # name on the title bar of the window  




FPS=10 

lead_x=display_height/2
lead_y=display_width/2
lead_x_change = 0
lead_y_change = 0

block_size =10

clock = pygame.time.Clock() # for fps 


while not gameExit:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            gameExit= True

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
##                lead_x_change=0
##            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
##                lead_y_change=0

        if lead_x > display_width  or lead_x < 0 or lead_y > display_height  or lead_y < 0:  # defining game area boundries.
            gameExit =True  
        
              
                
    lead_x +=lead_x_change
    lead_y +=lead_y_change

    pygame.time.Clock()
    
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,red, [lead_x, lead_y , block_size,block_size])

    clock.tick(FPS) # fps=5 
    
    
    pygame.display.update()
        
##        print(event)

pygame.quit()
quit()
