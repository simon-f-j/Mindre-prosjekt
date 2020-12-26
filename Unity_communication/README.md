# Communication with Unity trough UDP
**tl;dr:** <br/>
Simple way to update the position and orientation of an object in Unity trough data broadcast from other software/device trough UDP


**Background**:<br/>
This project is a continuation of some of the work carried out in my masters thesis, where i created a visualisation for simulations running in simulink. During the work with my thesis i was tasked with setting up a 'real-time' simulation of an electric ferry running in a 3d-environment. However i found there was not many publically available options that would work with Simulink. The motivation to use Simulink came from all the available libraries, especially for electriacl and mechanical systems. 

This led me to Unity, which were an easy alternative to set up a 3d model of the vessel and its environment to the degree i wanted. <br/><br/>
The solution i came up with was to let Simulink handle all the calculations of the model (since it's pretty good at that sort of thing), and broadcast the position and orientation of the vessel to Unity trough localhost UDP.<br/>
This approach i found to be working seamlessly after i spent a weekend setting up the Unity environment and running it whenever i start the model in Simulink. It also opens up the possibility to (maybe) use other devices dedicated to visualise the running simulation, as well as, (again maybe) build to tablets or phones. 

<br/>


![unity2](https://user-images.githubusercontent.com/72814986/103153405-907e6f80-4790-11eb-856c-fb64b7925e2c.PNG)
*Simplified 3d-environement from my thesis running in Real-Time*



The coordinates of the vessel is broadcast as a string containing coordinates for x,y,z as well as Euler angles φ, ψ and θ defining the orientation 




![unity1](https://user-images.githubusercontent.com/72814986/103153202-3204c180-478f-11eb-89d4-5bcd1d0cf958.PNG)
*Implementation of the communication script to a cube object*

**Setup**:<br/>
In Unity: for the object you want to move with data trough UDP, simply add the 'UDP_TRANSFORM.cs' to a component, and drag the object to the area named 'cube'<br/>
![unity4](https://user-images.githubusercontent.com/72814986/103153762-18fe0f80-4793-11eb-988d-06310206d12f.PNG)
<br/>
To test that everything works as intended, 'Unity_communication.py' can be used. This broadcasts a string of (x,z,y,φ,ψ,θ):<br/><br/>
Required packages for **python**:
- numpy


