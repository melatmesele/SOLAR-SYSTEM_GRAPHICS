import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from texture_loader import load_texture_pygame
from cameras import Cameras
from obj_loader import ObjLoader
import pyrr


class solar:
    
    def __init__(self):
        self.camera = Cameras()
        height, width = 1000, 800

        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode((height, width), pg.OPENGL |
                            pg.DOUBLEBUF | pg.RESIZABLE)
        glClearColor(1.3, 0.36, 0.34, 2.4)

        self.solar, self.planet_store = ObjLoader.load_model(
            "objects/solaaaaarrrrrrrr.obj", False)

        shader = self.Shadercreater(
            'shaders/vertex.txt', 'shaders/fragment.txt')

        VAO = glGenVertexArrays(1)
        VBO = glGenBuffers(1)
        
        glBindVertexArray(VAO)
        # solar Buffer Object
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.planet_store.nbytes,
                     self.planet_store, GL_STATIC_DRAW)


        # solar vertices
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE,
                              self.planet_store.itemsize * 8, ctypes.c_void_p(0))
        # solar textures
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE,
                              self.planet_store.itemsize * 8, ctypes.c_void_p(12))
        # solar normals
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE,
                              self.planet_store.itemsize * 8, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)

        # self.textures = glGenTextures(3)
        # self.textureloader()

        glUseProgram(shader)
        glClearColor(0, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.projection = pyrr.matrix44.create_perspective_projection_matrix(
            45, 1280 / 720, 0.1, 100)
        self.car_pos = pyrr.matrix44.create_from_translation(
            pyrr.Vector3([6, 4, 0]))
        self.road_pos = pyrr.matrix44.create_from_translation(
            pyrr.Vector3([-4, 4, -4]))
        self.environment_pos = pyrr.matrix44.create_from_translation(
            pyrr.Vector3([0, 0, 0]))

        self.model_loc = glGetUniformLocation(shader, "model")
        self.proj_loc = glGetUniformLocation(shader, "projection")
        self.view_loc = glGetUniformLocation(shader, "view")

        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, self.projection)

        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                    running = False
                if event.type == pg.VIDEORESIZE:
                    glViewport(0, 0, event.w, event.h)
                    projection = pyrr.matrix44.create_perspective_projection_matrix(
                        45, event.w / event.h, 0.1, 100)
                    glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, projection)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            view = self.camera.get_view_matrix()
            glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, view)

            self.draw(0, self.solar)

            pg.display.flip()

    
       

    # def textureloader(self):
    #     if not self.carcolorchange:
    #         load_texture_pygame("textures/car.jpg", self.textures[0])
    #     else:
    #         load_texture_pygame("textures/black.jpg", self.textures[0])
    #     load_texture_pygame("textures/road.jpg", self.textures[1])
    #     load_texture_pygame("textures/grass.jpg", self.textures[2])

    def Shadercreater(self, vertexFilepath, fragmentFilepath):

        with open(vertexFilepath, 'r') as f:
            vertex_src = f.readlines()

        with open(fragmentFilepath, 'r') as f:
            fragment_src = f.readlines()

        shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                                compileShader(fragment_src, GL_FRAGMENT_SHADER))

        return shader

    
        

    def draw(self, index, indices):
        rot_y = pyrr.Matrix44.from_y_rotation(0.2)
        model = pyrr.matrix44.multiply(rot_y, self.car_pos)
        glBindVertexArray(self.VAO[index])
        # glBindTexture(GL_TEXTURE_2D, self.textures[index])
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, model)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    def quit(self):
       
        glDeleteVertexArrays(1, (self.VAO,))
        glDeleteBuffers(1,(self.VBO,))
        pg.quit()
if __name__ == "__main__":

    dd = solar()
