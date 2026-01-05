from pyscript import document

def clubbing(event):
    club=document.getElementById("club").value
    info_box=document.getElementById("info")
    output=document.getElementById("clubinfo")
    info_box.style.display="block"
    clubs_info={
        "choose":"Please select a club from the dropdown to see information.",
        "club1":"Robotics Club\nDesign, build, and program robots. Participate in competitions, learn engineering, coding, and teamwork skills.",
        "club2":"Art Society\nExplore painting, drawing, sculpture, and digital arts. Participate in workshops and exhibitions every semester.",
        "club3":"Debate Team\nSharpen public speaking, critical thinking, and argumentation skills. Compete in local and national tournaments.",
        "club4":"Chess Club\nPlay chess at all skill levels. Join tournaments and improve strategy and focus.",
        "club5":"Music Ensemble\nParticipate in orchestras, choirs, and bands. Perform at events and festivals.",
        "club6":"Coding Club\nLearn programming, work on projects, and compete in hackathons.",
        "club7":"Sports Society\nEngage in football, basketball, swimming, and more. Promote teamwork and health.",
        "club8":"Environmental Club\nFocus on sustainability projects, campaigns, and eco-friendly initiatives.",
        "club9":"Drama Club\nParticipate in theatre productions, improv nights, and stagecraft workshops.",
        "club10":"Photography Society\nLearn photography skills, go on photo walks, and showcase work in exhibitions."
    }
    output.innerText=clubs_info.get(club,"Club information not available.")