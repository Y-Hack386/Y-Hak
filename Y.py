U
    ��N_  �                   @   s�   d dl Z d dlZe �d� dZdZdZdZdZdZd	Z	d
Z
dd� ZdZer�e�  ed� ed�ZedkrFe �d� ed� e �d� ed� e �d� ed� ed�Zedkr�e �d� e�  ed�ZqFq�qFdS )�    N�clearz[1;30mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[1;37mc                   C   s�   t td � t�d� t td � t�d� t td � t�d� t td � t�d� t td � t�d� t d� t d� t d� t�d� t d	� t�d� t d� d S )
Nz__   __    _   _       _   g�������?z\ \ / /   | | | | __ _| | __   z \ V /____| |_| |/ _` | |/ / z  | |_____|  _  | (_| |   <  z  |_|     |_| |_|\__,_|_|\_\  � z$[1;32m[1][1;31mpkg [1;34minstall z[2] Exit)�print�R�time�sleep� r   r   �Y.py�banner   s"    






r
   Tr   zWrite Your Option==>�1zstart install...{update}z	pkg udatezstart install...{upgrade}zpkg upgradezfinsh All install pkg)�osr   �system�Br   �G�Y�b�P�C�Wr
   Zloopr   �input�Tr   r   r   r	   �<module>   s:   





