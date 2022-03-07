import React from "react";

import {
  Section,
  SectionText,
  SectionTitle,
} from "../../styles/GlobalComponents";
import Button from "../../styles/GlobalComponents/Button";
import { LeftSection } from "./HeroStyles";

const Hero = (props) => (
  <Section row nopadding>
    <LeftSection>
      <SectionTitle main center>
        NFNTKID.JS
        <br />
      </SectionTitle>
      <SectionText>
        Music producer, Artist, Developer, & Teacher
        <br />
        "The Future is Data"
      </SectionText>
      <Button onclick={() => (window.location = "https://nfntny.com")}>
        Explore the Infinite
      </Button>
    </LeftSection>
  </Section>
);

export default Hero;
