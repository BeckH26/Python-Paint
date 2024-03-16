import pygame


class Tiles:

    def __init__(self, w, h, window, white, grey, red, orange, yellow, green, blue, purple, black):
        self.w = w
        self.h = h
        self.window = window
        self.white = white
        self.grey = grey
        self.red = red
        self.rows = int(h/4)
        self.cols = int(w/4)
        self.orange = orange
        self.yellow = yellow
        self.green = green
        self.blue = blue
        self.purple = purple
        self.black = black
        self.tile_map = [[0 for i in range(self.cols)] for c in range(self.rows)]
        self.color = 'black'

    def create_map(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.tile_map[row][col] = 0
        #exit
        for w in range(self.cols-7, self.cols):
            for h in range(0, 7):
                self.tile_map[w][h] = 1
        self.tile_map[self.cols-6][1] = 7
        self.tile_map[self.cols-2][1] = 7
        self.tile_map[self.cols-5][2] = 7
        self.tile_map[self.cols-3][2] = 7
        self.tile_map[self.cols-4][3] = 7
        self.tile_map[self.cols-3][4] = 7
        self.tile_map[self.cols-5][4] = 7
        self.tile_map[self.cols-6][5] = 7
        self.tile_map[self.cols-2][5] = 7

        #save
        for w in range(self.cols-7, self.cols):
            for h in range(7, 14):
                self.tile_map[w][h] = 8
        self.tile_map[self.cols-6][8] = 0
        self.tile_map[self.cols-5][8] = 0
        self.tile_map[self.cols-6][9] = 0
        self.tile_map[self.cols-5][9] = 0
        self.tile_map[self.cols-4][9] = 0
        self.tile_map[self.cols-3][9] = 0
        self.tile_map[self.cols-2][9] = 0
        self.tile_map[self.cols-6][10] = 0
        self.tile_map[self.cols-5][10] = 0
        self.tile_map[self.cols-4][10] = 0
        self.tile_map[self.cols-3][10] = 0
        self.tile_map[self.cols-2][10] = 0
        self.tile_map[self.cols-6][11] = 0
        self.tile_map[self.cols-6][12] = 0
        self.tile_map[self.cols-2][11] = 0
        self.tile_map[self.cols-2][12] = 0

        #color selections
        for w in range(0, 7):
            for h in range(0, 49):
                self.tile_map[w][h] = 8
        for w in range(1, 6):
            for h in range(1, 6):
                self.tile_map[w][h] = 1
            for h in range(7, 12):
                self.tile_map[w][h] = 2
            for h in range(13, 18):
                self.tile_map[w][h] = 3
            for h in range(19, 24):
                self.tile_map[w][h] = 4
            for h in range(25, 30):
                self.tile_map[w][h] = 5
            for h in range(31, 36):
                self.tile_map[w][h] = 6
            for h in range(37, 42):
                self.tile_map[w][h] = 7
            for h in range(43, 48):
                self.tile_map[w][h] = 0
        return self.tile_map

    def draw_tiles(self):
        for row in range(self.rows):
            for col in range(self.cols):
                try:
                    if self.tile_map[row][col] == 0:
                        pygame.draw.rect(self.window, self.white, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 1:
                        pygame.draw.rect(self.window, self.red, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 2:
                        pygame.draw.rect(self.window, self.orange, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 3:
                        pygame.draw.rect(self.window, self.yellow, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 4:
                        pygame.draw.rect(self.window, self.green, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 5:
                        pygame.draw.rect(self.window, self.blue, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 6:
                        pygame.draw.rect(self.window, self.purple, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 7:
                        pygame.draw.rect(self.window, self.black, (row*4, col*4, 1*4, 1*4))
                    elif self.tile_map[row][col] == 8:
                        pygame.draw.rect(self.window, self.grey, (row*4, col*4, 1*4, 1*4))
                except:
                    print('error')


    def draw(self):
        color = True
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                x, y = event.pos
                x = int(x/4)
                y = int(y/4)

                #exit button
                if x in range(self.cols-7, self.cols) and y in range(0, 7):
                    pygame.quit()
                    exit()

                #save button
                if x in range(self.cols-7, self.cols) and y in range(7, 14):
                    pygame.image.save(self.window, "painting.jpg")
                    color = False

                if x not in range(0,7) or y not in range(0, 49):
                    if color == True:
                        try:
                            if self.color == 'red':
                                self.tile_map[x][y] = 1
                            if self.color == 'orange':
                                self.tile_map[x][y] = 2
                            if self.color == 'yellow':
                                self.tile_map[x][y] = 3
                            if self.color == 'green':
                                self.tile_map[x][y] = 4
                            if self.color == 'blue':
                                self.tile_map[x][y] = 5
                            if self.color == 'purple':
                                self.tile_map[x][y] = 6
                            if self.color == 'black':
                                self.tile_map[x][y] = 7
                            if self.color == 'grey':
                                self.tile_map[x][y] = 8
                            if self.color == 'white':
                                self.tile_map[x][y] = 0
                        except:
                            continue
                else:
                    if x in range(1, 6) and y in range(1, 6):
                        self.color = 'red'
                    if x in range(1, 6) and y in range(7, 12):
                        self.color = 'orange'
                    if x in range(1, 6) and y in range(13, 18):
                        self.color = 'yellow'
                    if x in range(1, 6) and y in range(19, 24):
                        self.color = 'green'
                    if x in range(1, 6) and y in range(25, 30):
                        self.color = 'blue'
                    if x in range(1, 6) and y in range(31, 36):
                        self.color = 'purple'
                    if x in range(1, 6) and y in range(37, 42):
                        self.color = 'black'
                    if x in range(1, 6) and y in range(43, 48):
                        self.color = 'white'

                color = True