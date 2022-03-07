import React from "react";
import {
  DiAngularSimple,
  DiApple,
  DiAtom,
  DiBootstrap,
  DiCode,
  DiDatabase,
  DiDjango,
  DiFirebase,
  DiLinux,
  DiReact,
  DiZend,
} from "react-icons/di";
import {
  Section,
  SectionDivider,
  SectionText,
  SectionTitle,
} from "../../styles/GlobalComponents";
import {
  List,
  ListContainer,
  ListItem,
  ListParagraph,
  ListTitle,
} from "./TechnologiesStyles";

/* 
Make a section containing the technologies that you have worked with.
                    ***Intensive experience***
*/
const Technologies = () => (
  <Section id="tech">
    <SectionDivider />
    <SectionTitle>Technologies</SectionTitle>
    <SectionText>
      I've worked include a wide range of technologies from data frameworks to
      Ui/Ux
    </SectionText>
    <List>
      <ListItem>
        <DiCode size="3rem" />
        <ListContainer>
          <ListTitle>Front-End</ListTitle>
          <ListParagraph>
            React.js <br />
            Bootstrap
          </ListParagraph>
        </ListContainer>
      </ListItem>

      <ListItem>
        <DiAtom size="3rem" />
        <ListContainer>
          <ListTitle>Back-End</ListTitle>
          <ListParagraph>
            Node.js <br />
            Flask <br />
            Django <br />
          </ListParagraph>
        </ListContainer>
      </ListItem>

      <ListItem>
        <DiDatabase size="3rem" />
        <ListContainer>
          <ListTitle>Data</ListTitle>
          <ListParagraph>
            Numpy <br />
            Pandas <br />
            Selenium <br />
            bs4 <br />
            SQL <br />
          </ListParagraph>
        </ListContainer>
      </ListItem>
    </List>
  </Section>
);

export default Technologies;
